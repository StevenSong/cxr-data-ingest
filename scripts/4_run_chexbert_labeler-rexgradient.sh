DATA_DIR=/opt/gpudata/cxr/rexgradient/metadata

python chexbert-labeler.py --reports_path $DATA_DIR/train_metadata.csv --output_path $DATA_DIR/train_chexbert_labels.csv --id_col id --report_cols Findings Impression
python chexbert-labeler.py --reports_path $DATA_DIR/valid_metadata.csv --output_path $DATA_DIR/valid_chexbert_labels.csv --id_col id --report_cols Findings Impression
python chexbert-labeler.py --reports_path $DATA_DIR/test_metadata.csv --output_path $DATA_DIR/test_chexbert_labels.csv --id_col id --report_cols Findings Impression
