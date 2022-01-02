## Generating Evaluation Tables
The zip files for our workflow run are in `alloopslaartifacts.tar.gz`, first extract it:
```
tar -xvzf alloopslaartifacts.tar.gz
```
The above command will generate `all3cartifacts` folder in the current directory that contains all our zip file.

Assuming that `all3cartifacts` is in your folder i.e., `~/all3cartifacts`, you can use the following scripts to generate the tables (in Latex format) that we used in the camera ready version of the paper.

> For Artifact evaluation committe: the numbers in the submitted version might differ very slightly with these numbers because of the new improvements we made to 3C while the paper is in submission. We will be using these numbers in the camera ready version of the paper.

**Note: You can generate new tables from fresh runs by first downloading all artifacts of workflow runs in to a folder (using  `download_artifacts.py`) and use it in the following scripts.**

#### Generating Checked Pointer Stats
The script `generate_pointer_stats.py` will generate the following tables in the Latex format:
  * Pointer stats table (checked pointers inferred by our technique v/s CCured) - Table 3 in the paper.
  * Wild pointer stats (number and categories of Wild pointers and their root causes) - Table 7 in the supplementary material.
  * Pointer stats without macro expansion - Table 8 in the supplementary material.
```
python3.8 stats_scripts/generate_pointer_stats.py ~/all3cartifacts
Table 3 (Pointers inferred by 3c v/s CCured)

\rowcolor{black!15} vsftpd & 1,766 & \textbf{1,337 (75.71\%)} & 1,218 (68.97\%) & 991 (56.12\%) & 93 (6.96\%) & 44 (3.29\%) & \textbf{1,200 (89.75\%)}  \\
icecast & 2,683 & \textbf{1,796 (66.94\%)} & 1,676 (62.47\%) & 1,374 (51.21\%) & 312 (17.37\%) & 54 (3.01\%) & \textbf{1,430 (79.62\%)}  \\
\rowcolor{black!15} lua & 4,176 & \textbf{2,781 (66.59\%)} & 2,248 (53.83\%) & 1,771 (42.41\%) & 254 (9.13\%) & 254 (9.13\%) & \textbf{2,273 (81.73\%)}  \\
olden & 836 & \textbf{725 (86.72\%)} & 714 (85.41\%) & 716 (85.65\%) & 20 (2.76\%) & 130 (17.93\%) & \textbf{575 (79.31\%)}  \\
\rowcolor{black!15} parson & 686 & \textbf{507 (73.91\%)} & 425 (61.95\%) & 291 (42.42\%) & 93 (18.34\%) & 9 (1.78\%) & \textbf{405 (79.88\%)}  \\
ptrdist & 901 & \textbf{609 (67.59\%)} & 573 (63.6\%) & 550 (61.04\%) & 30 (4.93\%) & 163 (26.77\%) & \textbf{416 (68.31\%)}  \\
\rowcolor{black!15} zlib & 647 & \textbf{385 (59.51\%)} & 375 (57.96\%) & 337 (52.09\%) & 6 (1.56\%) & 86 (22.34\%) & \textbf{293 (76.1\%)}  \\
libtiff & 3,478 & \textbf{2,111 (60.7\%)} & 2,016 (57.96\%) & 1,194 (34.33\%) & 240 (11.37\%) & 177 (8.38\%) & \textbf{1,694 (80.25\%)}  \\
\rowcolor{black!15} libarchive & 10,269 & \textbf{6,842 (66.63\%)} & 6,190 (60.28\%) & 4,924 (47.95\%) & 414 (6.05\%) & 896 (13.1\%) & \textbf{5,532 (80.85\%)}  \\
thttpd & 829 & \textbf{634 (76.48\%)} & 616 (74.31\%) & 449 (54.16\%) & 236 (37.22\%) & 57 (8.99\%) & \textbf{341 (53.79\%)}  \\
\rowcolor{black!15} tinybignum & 129 & \textbf{128 (99.22\%)} & 117 (90.7\%) & 117 (90.7\%) & 15 (11.72\%) & 3 (2.34\%) & \textbf{110 (85.94\%)}  \\
\midrule
\textbf{Total} & 26,400 & \textbf{17,855 (67.63\%)} & 16,168 (61.24\%) & 12,714 (48.16\%)1,713 (9.59\%) & 1,873 (10.49\%) & \textbf{14,269 (79.92\%)}  \\
\bottomrule



Appendix A.1: Analysis of Wild Pointers (Table 7)
\rowcolor{black!15} vsftpd & 1,766 & 429 (24.29\%) & 218 (12.34\%) & 10 (0.57\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (64.37\%)\\Default void* type (16.9\%)\end{tabular} \\
icecast & 2,683 & 887 (33.06\%) & 337 (12.56\%) & 10 (0.37\%) & \begin{tabular}[c]{@{}c@{}}Source code in non-writable file. (28.97\%)\\Default void* type (24.2\%)\end{tabular} \\
\rowcolor{black!15} lua & 4,176 & 1,395 (33.41\%) & 308 (7.38\%) & 8 (0.19\%) & \begin{tabular}[c]{@{}c@{}}Union field encountered (76.1\%)\\Invalid Cast (10.83\%)\end{tabular} \\
olden & 836 & 111 (13.28\%) & 7 (0.84\%) & 6 (0.72\%) & \begin{tabular}[c]{@{}c@{}}Default void* type (56.8\%)\\Assigning from 0 depth pointer to 1 depth pointer. (36.4\%)\end{tabular} \\
\rowcolor{black!15} parson & 686 & 179 (26.09\%) & 99 (14.43\%) & 8 (1.17\%) & \begin{tabular}[c]{@{}c@{}}Inferred conflicting types (62.27\%)\\Invalid Cast (12.85\%)\end{tabular} \\
ptrdist & 901 & 292 (32.41\%) & 26 (2.89\%) & 17 (1.89\%) & \begin{tabular}[c]{@{}c@{}}Unsafe call to allocator function. (35.42\%)\\Unchecked pointer in parameter (27.51\%)\end{tabular} \\
\rowcolor{black!15} zlib & 647 & 262 (40.49\%) & 48 (7.42\%) & 6 (0.93\%) & \begin{tabular}[c]{@{}c@{}}Default void* type (51.06\%)\\Invalid Cast (32.22\%)\end{tabular} \\
libtiff & 3,478 & 1,367 (39.3\%) & 337 (9.69\%) & 11 (0.32\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (52.02\%)\\Union field encountered (13.84\%)\end{tabular} \\
\rowcolor{black!15} libarchive & 10,269 & 3,427 (33.37\%) & 897 (8.74\%) & 10 (0.1\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (58.89\%)\\Default void* type (18.75\%)\end{tabular} \\
thttpd & 829 & 195 (23.52\%) & 53 (6.39\%) & 7 (0.84\%) & \begin{tabular}[c]{@{}c@{}}Default void* type (51.13\%)\\Source code in non-writable file. (27.57\%)\end{tabular} \\
\rowcolor{black!15} tinybignum & 129 & 1 (0.78\%) & 0 (0.0\%) & 1 (0.78\%) & \begin{tabular}[c]{@{}c@{}}Source code in non-writable file. (100.0\%)\end{tabular} \\
\midrule
\textbf{Total} & 26,400 & 8,545 (32.37\%) & 2,330 (8.83\%) & 94 (0.36\%) &  \\
\bottomrule



Appendix A.2: Without macro expansion (Table 8)
\midrule
\rowcolor{black!15} vsftpd$_{m}$ & 1,766 & \textbf{1,336 (75.65\%)} & 1,227 (69.48\%) & 991 (56.12\%) & 430 (24.35\%) & 218 (12.34\%) & 9 (0.51\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (66.55\%)\\Default void* type (14.98\%)\end{tabular} & \\
icecast$_{m}$ & 2,677 & \textbf{1,790 (66.87\%)} & 1,670 (62.38\%) & 1,383 (51.66\%) & 887 (33.13\%) & 337 (12.59\%) & 10 (0.37\%) & \begin{tabular}[c]{@{}c@{}}Source code in non-writable file. (27.39\%)\\Default void* type (26.55\%)\end{tabular} & \\
\rowcolor{black!15} lua$_{m}$ & 3,999 & \textbf{2,040 (51.01\%)} & 1,713 (42.84\%) & 1,484 (37.11\%) & 1,959 (48.99\%) & 503 (12.58\%) & 9 (0.23\%) & \begin{tabular}[c]{@{}c@{}}Pointer in Macro (28.02\%)\\Invalid Cast (25.91\%)\end{tabular} & \\
olden$_{m}$ & 836 & \textbf{638 (76.32\%)} & 627 (75.0\%) & 617 (73.8\%) & 198 (23.68\%) & 7 (0.84\%) & 10 (1.2\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (66.67\%)\\Unsafe call to allocator function. (25.0\%)\end{tabular} & \\
\rowcolor{black!15} parson$_{m}$ & 686 & \textbf{484 (70.55\%)} & 351 (51.17\%) & 291 (42.42\%) & 202 (29.45\%) & 99 (14.43\%) & 8 (1.17\%) & \begin{tabular}[c]{@{}c@{}}Inferred conflicting types (60.67\%)\\Source code in non-writable file. (16.78\%)\end{tabular} & \\
ptrdist$_{m}$ & 901 & \textbf{483 (53.61\%)} & 457 (50.72\%) & 436 (48.39\%) & 418 (46.39\%) & 28 (3.11\%) & 19 (2.11\%) & \begin{tabular}[c]{@{}c@{}}Default void* type (62.5\%)\\Invalid Cast (37.5\%)\end{tabular} & \\
\rowcolor{black!15} zlib$_{m}$ & 647 & \textbf{146 (22.57\%)} & 141 (21.79\%) & 106 (16.38\%) & 501 (77.43\%) & 57 (8.81\%) & 7 (1.08\%) & \begin{tabular}[c]{@{}c@{}}Pointer in Macro (68.2\%)\\Invalid Cast (18.85\%)\end{tabular} & \\
libtiff$_{m}$ & 3,448 & \textbf{1,935 (56.12\%)} & 1,850 (53.65\%) & 1,176 (34.11\%) & 1,513 (43.88\%) & 361 (10.47\%) & 12 (0.35\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (78.34\%)\\Default void* type (7.23\%)\end{tabular} & \\
\rowcolor{black!15} libarchive$_{m}$ & 10,261 & \textbf{6,785 (66.12\%)} & 6,158 (60.01\%) & 4,918 (47.93\%) & 3,476 (33.88\%) & 937 (9.13\%) & 11 (0.11\%) & \begin{tabular}[c]{@{}c@{}}Invalid Cast (58.19\%)\\Default void* type (20.01\%)\end{tabular} & \\
thttpd$_{m}$ & 829 & \textbf{631 (76.12\%)} & 615 (74.19\%) & 448 (54.04\%) & 198 (23.88\%) & 54 (6.51\%) & 8 (0.97\%) & \begin{tabular}[c]{@{}c@{}}Default void* type (46.97\%)\\Source code in non-writable file. (26.91\%)\end{tabular} & \\
\rowcolor{black!15} tinybignum$_{m}$ & 129 & \textbf{128 (99.22\%)} & 117 (90.7\%) & 117 (90.7\%) & 1 (0.78\%) & 0 (0.0\%) & 1 (0.78\%) & \begin{tabular}[c]{@{}c@{}}Source code in non-writable file. (100.0\%)\end{tabular} & \\
\midrule
\textbf{Total} & 26,179 & \textbf{16,396 (62.63\%)} & 14,926 (57.02\%) & 11,967 (45.71\%) & 9,783 (37.37\%) & 2,601 (9.94\%) & 104 (0.4\%) &  & \\
\bottomrule
```
#### Generating Bounds and Timing Stats
The script `generate_bounds_timings.py` will generate bounds and timing stats in the Latex format:
  * Bounds stats table (effectiveness of our bounds inference technique) - Table 4 in the paper.
  * Timing stats (split of the time spent in each of the phases) - We will add this information in the camera ready.

```
python3.8 stats_scripts/generate_bounds_timings.py ~/all3cartifacts
Bounds Table (Table 4)

\rowcolor{black!15} vsftpd & 30 & 26 (86.67\%) & 15 (57.69\%) & 6 (23.08\%) & 5 (19.23\%) & 27 & 18 (66.67\%) & 17 (94.44\%) & 1 (5.56\%) \\
icecast & 29 & 21 (72.41\%) & 17 (80.95\%) & 4 (19.05\%) & 0 (0.0\%) & 159 & 60 (37.74\%) & 48 (80.0\%) & 12 (20.0\%) \\
\rowcolor{black!15} lua & 146 & 79 (54.11\%) & 61 (77.22\%) & 18 (22.78\%) & 0 (0.0\%) & 99 & 28 (28.28\%) & 18 (64.29\%) & 10 (35.71\%) \\
olden & 91 & 84 (92.31\%) & 67 (79.76\%) & 17 (20.24\%) & 0 (0.0\%) & 0 & 0 (0.0\%) & 0 (0.0\%) & 0 (0.0\%) \\
\rowcolor{black!15} parson & 2 & 2 (100.0\%) & 2 (100.0\%) & 0 (0.0\%) & 0 (0.0\%) & 33 & 22 (66.67\%) & 12 (54.55\%) & 10 (45.45\%) \\
ptrdist & 109 & 68 (62.39\%) & 47 (69.12\%) & 21 (30.88\%) & 0 (0.0\%) & 9 & 3 (33.33\%) & 2 (66.67\%) & 1 (33.33\%) \\
\rowcolor{black!15} zlib & 52 & 50 (96.15\%) & 37 (74.0\%) & 12 (24.0\%) & 1 (2.0\%) & 1 & 0 (0.0\%) & 0 (0.0\%) & 0 (0.0\%) \\
libtiff & 65 & 65 (100.0\%) & 42 (64.62\%) & 23 (35.38\%) & 0 (0.0\%) & 145 & 145 (100.0\%) & 144 (99.31\%) & 1 (0.69\%) \\
\rowcolor{black!15} libarchive & 449 & 352 (78.4\%) & 256 (72.73\%) & 87 (24.72\%) & 9 (2.56\%) & 112 & 42 (37.5\%) & 28 (66.67\%) & 14 (33.33\%) \\
thttpd & 31 & 26 (83.87\%) & 19 (73.08\%) & 7 (26.92\%) & 0 (0.0\%) & 127 & 97 (76.38\%) & 61 (62.89\%) & 36 (37.11\%) \\
\rowcolor{black!15} tinybignum & 2 & 2 (100.0\%) & 2 (100.0\%) & 0 (0.0\%) & 0 (0.0\%) & 13 & 13 (100.0\%) & 13 (100.0\%) & 0 (0.0\%) \\
\midrule
\textbf{Total} & 1,006 & \textbf{775 (77.04\%)} & \textbf{565 (72.9\%)} & \textbf{195 (25.16\%)} & 15 (1.94\%) & 725 & \textbf{428 (59.03\%)} & \textbf{343 (47.31\%)} & \textbf{85 (11.72\%)} \\
\bottomrule



Timing Stats

ProgramName, Compile, ConGen, ConSol, ArrBounds, Rewrite, Total

\rowcolor{black!15} vsftpd & 1.3 (34.21\%) & 0.58 (15.18\%) & 0.24 (6.24\%) & 0.27 (7.11\%) & 1.39 (36.57\%) & 3.81 \\
icecast & 7.88 (46.18\%) & 1.58 (9.29\%) & 1.92 (11.27\%) & 1.55 (9.11\%) & 3.81 (22.35\%) & 17.06 \\
\rowcolor{black!15} lua & 2.59 (35.66\%) & 1.33 (18.31\%) & 0.53 (7.29\%) & 0.89 (12.31\%) & 1.84 (25.34\%) & 7.26 \\
olden & 1.85 (61.77\%) & 0.28 (9.32\%) & 0.34 (11.49\%) & 0.13 (4.35\%) & 0.37 (12.35\%) & 2.99 \\
\rowcolor{black!15} parson & 0.26 (38.44\%) & 0.18 (27.2\%) & 0.05 (6.77\%) & 0.11 (16.34\%) & 0.09 (13.79\%) & 0.67 \\
ptrdist & 1.3 (52.34\%) & 0.4 (16.0\%) & 0.28 (11.43\%) & 0.17 (6.84\%) & 0.33 (13.41\%) & 2.49 \\
\rowcolor{black!15} zlib & 1.06 (46.84\%) & 0.52 (23.1\%) & 0.16 (7.09\%) & 0.16 (6.93\%) & 0.33 (14.46\%) & 2.26 \\
libtiff & 3.82 (37.35\%) & 1.93 (18.86\%) & 0.85 (8.32\%) & 0.99 (9.68\%) & 2.51 (24.49\%) & 10.24 \\
\rowcolor{black!15} libarchive & 18.73 (30.31\%) & 5.72 (9.26\%) & 4.57 (7.39\%) & 13.06 (21.14\%) & 19.04 (30.82\%) & 61.8 \\
thttpd & 1.01 (41.83\%) & 0.49 (20.11\%) & 0.2 (8.4\%) & 0.36 (14.9\%) & 0.33 (13.84\%) & 2.41 \\
\rowcolor{black!15} tinybignum & 0.25 (50.8\%) & 0.07 (13.83\%) & 0.09 (18.26\%) & 0.02 (3.94\%) & 0.06 (12.73\%) & 0.49 \\
\midrule
\textbf{Total} & 40.05 (35.93\%) & 13.08 (11.74\%) & 9.23 (8.28\%) & 17.72 (15.89\%) & 30.11 (27.02\%) & 111.47 \\
\bottomrule
```

#### Generating Least/Greatest/Our solution stats

The script `generate_least_greatest_table.py` will generate table comparing the effectiveness of our solution v/s least v/s greatest solution:
  * Solution effectivness table -  Table 9 in the supplementary material.
 
 ```
 /usr/bin/python3.8 stats_scripts/generate_least_greatest_table.py ~/all3cartifacts
Appendix A.3 Our solution v/s least v/s greatest (Table 9)

\rowcolor{black!15} vsftpd & 1,337 & 93 (6.96\%) & 93 (6.96\%) & \textcolor{red}{197 (14.73\%)} & 44 (3.29\%) & 44 (3.29\%) & \textcolor{red}{638 (47.72\%)} & 1,200 (89.75\%) & 1,200 (89.75\%) & \textcolor{red}{502 (37.55\%)} \\
icecast & 1,796 & 312 (17.37\%) & \textcolor{red}{309 (17.2\%)} & \textcolor{red}{536 (29.84\%)} & 54 (3.01\%) & 54 (3.01\%) & \textcolor{red}{412 (22.94\%)} & 1,430 (79.62\%) & \textcolor{red}{1,433 (79.79\%)} & \textcolor{red}{848 (47.22\%)} \\
\rowcolor{black!15} lua & 2,781 & 254 (9.13\%) & 254 (9.13\%) & \textcolor{red}{587 (21.11\%)} & 254 (9.13\%) & 254 (9.13\%) & \textcolor{red}{622 (22.37\%)} & 2,273 (81.73\%) & 2,273 (81.73\%) & \textcolor{red}{1,572 (56.53\%)} \\
olden & 725 & 20 (2.76\%) & \textcolor{red}{17 (2.34\%)} & \textcolor{red}{114 (15.72\%)} & 130 (17.93\%) & \textcolor{red}{128 (17.66\%)} & \textcolor{red}{212 (29.24\%)} & 575 (79.31\%) & \textcolor{red}{580 (80.0\%)} & \textcolor{red}{399 (55.03\%)} \\
\rowcolor{black!15} parson & 507 & 93 (18.34\%) & 93 (18.34\%) & \textcolor{red}{114 (22.49\%)} & 9 (1.78\%) & 9 (1.78\%) & \textcolor{red}{277 (54.64\%)} & 405 (79.88\%) & 405 (79.88\%) & \textcolor{red}{116 (22.88\%)} \\
ptrdist & 609 & 30 (4.93\%) & \textcolor{red}{29 (4.76\%)} & \textcolor{red}{164 (26.93\%)} & 163 (26.77\%) & \textcolor{red}{162 (26.6\%)} & \textcolor{red}{238 (39.08\%)} & 416 (68.31\%) & \textcolor{red}{418 (68.64\%)} & \textcolor{red}{207 (33.99\%)} \\
\rowcolor{black!15} zlib & 385 & 6 (1.56\%) & 6 (1.56\%) & \textcolor{red}{136 (35.32\%)} & 86 (22.34\%) & 86 (22.34\%) & \textcolor{red}{198 (51.43\%)} & 293 (76.1\%) & 293 (76.1\%) & \textcolor{red}{51 (13.25\%)} \\
libtiff & 2,111 & 240 (11.37\%) & 240 (11.37\%) & \textcolor{red}{610 (28.9\%)} & 177 (8.38\%) & 177 (8.38\%) & \textcolor{red}{1,220 (57.79\%)} & 1,694 (80.25\%) & 1,694 (80.25\%) & \textcolor{red}{281 (13.31\%)} \\
\rowcolor{black!15} libarchive & 6,842 & 414 (6.05\%) & 414 (6.05\%) & \textcolor{red}{1,737 (25.39\%)} & 896 (13.1\%) & 896 (13.1\%) & \textcolor{red}{2,571 (37.58\%)} & 5,532 (80.85\%) & 5,532 (80.85\%) & \textcolor{red}{2,534 (37.04\%)} \\
thttpd & 634 & 236 (37.22\%) & 236 (37.22\%) & \textcolor{red}{375 (59.15\%)} & 57 (8.99\%) & 57 (8.99\%) & \textcolor{red}{163 (25.71\%)} & 341 (53.79\%) & 341 (53.79\%) & \textcolor{red}{96 (15.14\%)} \\
\rowcolor{black!15} tinybignum & 128 & 15 (11.72\%) & 15 (11.72\%) & \textcolor{red}{19 (14.84\%)} & 3 (2.34\%) & 3 (2.34\%) & \textcolor{red}{54 (42.19\%)} & 110 (85.94\%) & 110 (85.94\%) & \textcolor{red}{55 (42.97\%)} \\
\midrule
\textbf{Total} & 17,855 & 1,713 (9.59\%) & \textcolor{red}{1,706 (9.55\%)} & \textcolor{red}{4,589 (25.7\%)} & 1,873 (10.49\%) & 1,870 (10.47\%) & \textcolor{red}{6,605 (36.99\%)} & 14,269 (79.92\%) & \textcolor{red}{14,279 (79.97\%)} & \textcolor{red}{6,661 (37.31\%)} \\
\bottomrule
 ```
