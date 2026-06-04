import argparse

import numpy as np
import pandas as pd
from f1chexbert import F1CheXbert
from tqdm import tqdm

CHEXPERT_LABEL_ORDER = [
    "No Finding",
    "Enlarged Cardiomediastinum",
    "Cardiomegaly",
    "Lung Lesion",
    "Lung Opacity",
    "Edema",
    "Consolidation",
    "Pneumonia",
    "Atelectasis",
    "Pneumothorax",
    "Pleural Effusion",
    "Pleural Other",
    "Fracture",
    "Support Devices",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports_path", required=True)
    parser.add_argument("--output_path", required=True)
    parser.add_argument("--id_col")
    parser.add_argument("--report_cols", nargs="+")
    args = parser.parse_args()
    return args


def main(
    *,  # enforce kwargs
    reports_path: str,
    output_path: str,
    id_col: str | None,
    report_cols: list[str] | None,
):
    model = F1CheXbert()
    label_to_model_idx = {k: i for i, k in enumerate(model.target_names)}
    model_idxs = [label_to_model_idx[l] for l in CHEXPERT_LABEL_ORDER]
    header = "infer"
    if report_cols is None or len(report_cols) == 0:
        report_cols = [0]  # type: ignore
        header = None
    assert report_cols is not None

    all_reports = pd.read_csv(reports_path, header=header)
    data: dict[tuple[str, str], list] = dict()
    if id_col is not None:
        data[(id_col, "")] = all_reports[id_col].to_list()

    # label reports
    for report_col in report_cols:
        reports = all_reports[report_col].to_list()
        data[(report_col, "Reports")] = reports
        labels = []
        for report in tqdm(reports, desc=f"Labeling Reports in Column: {report_col}"):
            per_report_labels = model.get_label(report)
            labels.append(per_report_labels)
        labels = np.asarray(labels)  # (N, L)
        for label_name, idx in zip(CHEXPERT_LABEL_ORDER, model_idxs):
            data[(report_col, label_name)] = labels[:, idx].tolist()

    df = pd.DataFrame(data=data)
    if header is None:  # single col
        cols = ["Reports"] + CHEXPERT_LABEL_ORDER
        if id_col is not None:
            cols = ["study_id"] + cols
        df.columns = cols
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    args = parse_args()
    main(
        reports_path=args.reports_path,
        output_path=args.output_path,
        id_col=args.id_col,
        report_cols=args.report_cols,
    )
