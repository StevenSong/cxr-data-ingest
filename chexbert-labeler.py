import argparse

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
    args = parser.parse_args()
    return args


def main(reports_path: str, output_path: str):
    model = F1CheXbert()
    reports = pd.read_csv(reports_path, header=None)[0].to_list()
    data = []
    for report in tqdm(reports):
        labels = model.get_label(report)
        data.append([report] + labels)
    df = pd.DataFrame(data=data, columns=["Reports"] + model.target_names)
    df = df.loc[:, ["Reports"] + CHEXPERT_LABEL_ORDER]
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    args = parse_args()
    main(
        reports_path=args.reports_path,
        output_path=args.output_path,
    )
