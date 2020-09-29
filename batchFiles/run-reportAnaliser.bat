call cd ..
call python reportAnaliser.py -i EncodeDS/* -ur Reports-ruleValidator/ruleValidator-FS1/* -r Rules/fs-1__sup_02-conf_1.csv -s directory -f finalReport -o fs-1.csv
call python reportAnaliser.py -i EncodeDS/* -ur Reports-ruleValidator/ruleValidator-FS2/* -r Rules/fs-2__sup_02-conf_1.csv -s directory -f finalReport -o fs-2.csv
call python reportAnaliser.py -i EncodeDS/* -ur Reports-ruleValidator/ruleValidator-FS3/* -r Rules/fs-3__sup_02-conf_1.csv -s directory -f finalReport -o fs-3.csv
call python reportAnaliser.py -i EncodeDS/* -ur Reports-ruleValidator/ruleValidator-FS4/* -r Rules/fs-4__sup_02-conf_1.csv -s directory -f finalReport -o fs-4.csv
call python reportAnaliser.py -i EncodeDS/* -ur Reports-ruleValidator/ruleValidator-FS5/* -r Rules/fs-5__sup_02-conf_1.csv -s directory -f finalReport -o fs-5.csv

call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS1/* -r Exp-uniqueRows/Rules/fs-1_ur__sup_02-conf_1.csv -s directory -f finalReport -o ur-fs-1.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS2/* -r Exp-uniqueRows/Rules/fs-2_ur__sup_02-conf_1.csv -s directory -f finalReport -o ur-fs-2.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS3/* -r Exp-uniqueRows/Rules/fs-3_ur__sup_02-conf_1.csv -s directory -f finalReport -o ur-fs-3.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS4/* -r Exp-uniqueRows/Rules/fs-4_ur__sup_02-conf_1.csv -s directory -f finalReport -o ur-fs-4.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS5/* -r Exp-uniqueRows/Rules/fs-5_ur__sup_02-conf_1.csv -s directory -f finalReport -o ur-fs-5.csv

call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows_2/Reports-ruleValidator/UR2-ruleValidator-FS1/* -r Exp-uniqueRows_2/Rules/merged_files/without-duplicates/fs-1_Rules_notRuleDuplicate.csv -s directory -f finalReport -o ur2-fs-1.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows_2/Reports-ruleValidator/UR2-ruleValidator-FS2/* -r Exp-uniqueRows_2/Rules/merged_files/without-duplicates/fs-2_Rules_notRuleDuplicate.csv -s directory -f finalReport -o ur2-fs-2.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows_2/Reports-ruleValidator/UR2-ruleValidator-FS3/* -r Exp-uniqueRows_2/Rules/merged_files/without-duplicates/fs-3_Rules_notRuleDuplicate.csv -s directory -f finalReport -o ur2-fs-3.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows_2/Reports-ruleValidator/UR2-ruleValidator-FS4/* -r Exp-uniqueRows_2/Rules/merged_files/without-duplicates/fs-4_Rules_notRuleDuplicate.csv -s directory -f finalReport -o ur2-fs-4.csv
call python reportAnaliser.py -i EncodeDS/* -ur Exp-uniqueRows_2/Reports-ruleValidator/UR2-ruleValidator-FS5/* -r Exp-uniqueRows_2/Rules/merged_files/without-duplicates/fs-5_Rules_notRuleDuplicate.csv -s directory -f finalReport -o ur2-fs-5.csv