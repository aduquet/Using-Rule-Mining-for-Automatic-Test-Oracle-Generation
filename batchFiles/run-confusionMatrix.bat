call cd..
call python confusionMatrix.py -i Reports-ruleValidator/ruleValidator-FS1/* -s dir -f confusionMatrix -o FS1-CM
call python confusionMatrix.py -i Reports-ruleValidator/ruleValidator-FS2/* -s dir -f confusionMatrix -o FS2-CM
call python confusionMatrix.py -i Reports-ruleValidator/ruleValidator-FS3/* -s dir -f confusionMatrix -o FS3-CM
call python confusionMatrix.py -i Reports-ruleValidator/ruleValidator-FS4/* -s dir -f confusionMatrix -o FS4-CM
call python confusionMatrix.py -i Reports-ruleValidator/ruleValidator-FS5/* -s dir -f confusionMatrix -o FS5-CM

call python confusionMatrix.py -i Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS1/* -s dir -f confusionMatrix -o UR_FS1-CM
call python confusionMatrix.py -i Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS2/* -s dir -f confusionMatrix -o UR_FS2-CM
call python confusionMatrix.py -i Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS3/* -s dir -f confusionMatrix -o UR_FS3-CM
call python confusionMatrix.py -i Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS4/* -s dir -f confusionMatrix -o UR_FS4-CM
call python confusionMatrix.py -i Exp-uniqueRows/Reports-ruleValidator/UR-ruleValidator-FS5/* -s dir -f confusionMatrix -o UR_FS5-CM

call python confusionMatrix.py -i Exp-uniqueRows_2/Reports-ruleValidator/UR-ruleValidator-FS1/* -s dir -f confusionMatrix -o UR2_FS1-CM
call python confusionMatrix.py -i Exp-uniqueRows_2/Reports-ruleValidator/UR-ruleValidator-FS2/* -s dir -f confusionMatrix -o UR2_FS2-CM
call python confusionMatrix.py -i Exp-uniqueRows_2/Reports-ruleValidator/UR-ruleValidator-FS3/* -s dir -f confusionMatrix -o UR2_FS3-CM
call python confusionMatrix.py -i Exp-uniqueRows_2/Reports-ruleValidator/UR-ruleValidator-FS4/* -s dir -f confusionMatrix -o UR2_FS4-CM
call python confusionMatrix.py -i Exp-uniqueRows_2/Reports-ruleValidator/UR-ruleValidator-FS5/* -s dir -f confusionMatrix -o UR2_FS5-CM
