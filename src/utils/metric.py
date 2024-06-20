import numpy as np

from sklearn.metrics import roc_curve, auc


def get_roc(labels: np.ndarray, scores: np.ndarray, max_fpr: float = 1.0):
    fpr, tpr, _ = roc_curve(labels, scores)

    fpr_auc = fpr[fpr <= max_fpr]
    tpr_auc = tpr[: len(fpr_auc)]

    roc_auc = auc(fpr, tpr)
    t_roc_auc = auc(fpr_auc, tpr_auc)

    return fpr.tolist(), tpr.tolist(), roc_auc, t_roc_auc
