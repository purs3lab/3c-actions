#!/usr/bin/env python3
# Filter the output of a build command for errors that should be ignored as
# likely reflecting known limitations of 3C bounds inference.
#
# usage: BUILD_COMMAND 2>&1 | filter-bounds-inference-errors.py
#
# Exits 1 if the input contains errors that should not be ignored. For this to
# be useful, the original pipeline should be run with `pipefail` off.

import re
import sys
import csv

# initialize counters and compile regexes
ERROR_LINE_RE = re.compile(r'^(.*): error: (.*)$')
seen_tags = {}
accepable_tags = {'ignore','bounds','inprogress'}
error_list = []
error_files = sys.argv[1:]
error_files.append("benchmark_errors.csv")
for file in error_files:
    try:
        with open(file,'r') as errors:
            error_list.extend([line for line in csv.DictReader(errors)])
    except Exception:
        pass
# prior whitelisted error for compatability
error_list.append({'category': "bounds", 'tag':"unknown_bounds", 'regex':"^expression has unknown bounds$"})
# final default error
error_list.append({'category': "error", 'tag':"UNKNOWN", 'regex':".*"})
for line in error_list:
    line['RE'] = re.compile(line['regex'])
    seen_tags[line['tag']] = 0

# read through errors incrementally, keeping stats
for line in sys.stdin:
    line = line.rstrip('\n')
    at_error = ERROR_LINE_RE.search(line)
    if at_error is not None:
        for error in error_list:
            if (error['RE'].search(at_error[2]) is not None):
                line = ERROR_LINE_RE.sub(r'\1: error ({}): \2'.format(error['tag']), line)
                seen_tags[error['tag']] += 1
                break
    # It probably makes more sense to write what was originally stderr output to
    # stderr rather than make all callers redirect it, even if unix convention
    # would normally be that the main data we process should go to stdout.
    sys.stderr.write(line + '\n')

# print out stats
output_tags = set()
seen_errors = 0
print()
print('Encountered errors:')
for e in error_list:
    if (e['tag'] in output_tags) or (seen_tags[e['tag']] == 0): continue
    output_tags.add(e['tag'])
    if e['category'] in accepable_tags:
        category = "(" + e['category'] + ")"
    else:
        seen_errors += seen_tags[e['tag']]
        category = "(error)"
    print('  {0}{1}: {2}     {3}'.format(category,e['tag'],seen_tags[e['tag']],e['note']))
if seen_errors > 0:
    print("Benchmark failed - {} errors not acceptable".format(seen_errors))
    sys.exit(1)
else:
    print("Benchmark succeeded - all errors acceptable")
    sys.exit(0)

