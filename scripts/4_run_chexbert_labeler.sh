DATA_DIR=/opt/gpudata/cxr-derived

# python chexbert-labeler.py --reports_path $DATA_DIR/mimic-findings.csv --output_path $DATA_DIR/mimic-findings-labels-chexbert.csv
# python chexbert-labeler.py --reports_path $DATA_DIR/mimic-impression.csv --output_path $DATA_DIR/mimic-impression-labels-chexbert.csv
# python chexbert-labeler.py --reports_path $DATA_DIR/chexpertplus-findings.csv --output_path $DATA_DIR/chexpertplus-findings-labels-chexbert.csv
# python chexbert-labeler.py --reports_path $DATA_DIR/chexpertplus-impression.csv --output_path $DATA_DIR/chexpertplus-impression-labels-chexbert.csv
python chexbert-labeler.py --reports_path $DATA_DIR/openi-findings.csv --output_path $DATA_DIR/openi-findings-labels-chexbert.csv
python chexbert-labeler.py --reports_path $DATA_DIR/openi-impression.csv --output_path $DATA_DIR/openi-impression-labels-chexbert.csv

# next step overwrites labeler output, backup labels
# cp $DATA_DIR/mimic-findings-labels-chexbert.csv $DATA_DIR/mimic-findings-labels-chexbert.csv.BAK
# cp $DATA_DIR/mimic-impression-labels-chexbert.csv $DATA_DIR/mimic-impression-labels-chexbert.csv.BAK
# cp $DATA_DIR/chexpertplus-findings-labels-chexbert.csv $DATA_DIR/chexpertplus-findings-labels-chexbert.csv.BAK
# cp $DATA_DIR/chexpertplus-impression-labels-chexbert.csv $DATA_DIR/chexpertplus-impression-labels-chexbert.csv.BAK
cp $DATA_DIR/openi-findings-labels-chexbert.csv $DATA_DIR/openi-findings-labels-chexbert.csv.BAK
cp $DATA_DIR/openi-impression-labels-chexbert.csv $DATA_DIR/openi-impression-labels-chexbert.csv.BAK
