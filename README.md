# Awesome-Medical-Image-Analysis-Fairness [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A collection of papers in fairness of medical image analysis

> For more details, please refer to our recent [survey on fairness in medical image analysis](https://arxiv.org/abs/2209.13177)
> 
> Notes: We may miss some relevant papers in the list. If you have any suggestions or would like to add some papers, please submit a pull request or email me at zikangxu@mail.ustc.edu.cn. Your contribution is much appreciated!
---
## Fairness Papers in Medical Image Analysis
### Fairness Evaluation
#### Unfairness Existence
1. Fairness-related performance and explainability effects in deep learning models for brain image analysis.JMI, 2022. ([paper](https://www.spiedigitallibrary.org/journals/journal-of-medical-imaging/volume-9/issue-6/061102/Fairness-related-performance-and-explainability-effects-in-deep-learning-models/10.1117/1.JMI.9.6.061102.short?SSO=1))
2. How fair is your graph? exploring fairness concerns in neuroimaging studies. ML4HC, 2022. ([paper](https://www.mlforhc.org/s/61-MHLC_61_Camera_Ready.pdf))
3. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature medicine,2021. ([paper](https://www.nature.com/articles/s41591-021-01595-0))
4. Fairness in cardiac magnetic resonance imaging: assessing sex and racial bias in deep learning-based segmentation. Frontiers in Cardiovascular Medicine, 2022. ([paper](https://www.frontiersin.org/articles/10.3389/fcvm.2022.859310/full?&utm_source=Email_to_authors_&utm_medium=Email&utm_content=T1_11.5e1_author&utm_campaign=Email_publication&field=&journalName=Frontiers_in_Cardiovascular_Medicine&id=859310))

#### Fairness & Data Distribution
1. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis. PNAS, 2020. ([paper](https://www.pnas.org/doi/full/10.1073/pnas.1919012117))
2. Algorithmic encoding of protected characteristics and its implications on disparities across subgroups. ArXiv, 2021. ([paper](https://arxiv.org/abs/2110.14755))
3. Feature robustness and sex differences in medical imaging: a case study in mri-based alzheimer’s disease detection. ArXiv, 2022. ([paper](https://arxiv.org/pdf/2204.01737))
4. Fairness of classifiers across skin tones in dermatology. MICCAI, 2020. ([paper](http://krvarshney.github.io/pubs/KinyanjuiOCCPSV_miccai2020.pdf))

#### Fairness Benchmarking
1. Improving the Fairness of Chest X-ray Classifiers. PCHIL, 2022. ([paper](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf))
2. Medfair: Benchmarking fairness for medical imaging. ICLR, 2023. ([paper](https://arxiv.org/abs/2210.01725), [code](https://github.com/ys-zong/MEDFAIR))

#### Fairness & Uncertainty
1. Evaluating subgroup disparity using epistemic uncertainty in mammography. ArXiv, 2021. ([paper](https://arxiv.org/abs/2107.02716))

#### Fairness & Model Selection
1. Model selection’s disparate impact in real-world deep learning applications. ArXiv, 2021. ([paper](https://arxiv.org/abs/2104.00606))

---
### Unfairness Mitigation via Pre-processing Methods
#### Data Resampling
1. Fairness in cardiac MR image analysis: An investigation of bias due to data imbalance in deep learning based segmentation. MICCAI, 2021. ([paper](https://link.springer.com/chapter/10.1007/978-3-030-87199-4_39))
2. Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short). ArXiv, 2022. ([paper](https://arxiv.org/pdf/2207.10384))

#### Data Synthesis
1. AI fairness via domain adaptation. ArXiv, 2021. ([paper](https://arxiv.org/pdf/2104.01109))
2.  CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions. ECCV-ISIC Workshop, 2022. ([paper](https://link.springer.com/chapter/10.1007/978-3-031-25069-9_14), [code](https://github.com/sfu-mial/CIRCLe))

#### Data Aggregation
1.  CheXclusion: Fairness gaps in deep chest X-ray classifiers. Proceedings of the Pacific Symposium, 2021. ([paper](https://healthyml.org/publication/seyyed-2020-chexclusion/))
2. Radfusion: Benchmarking performance and fairness for multimodal pulmonary embolism detection from ct and ehr. ArXiv, 2021. ([paper](https://arxiv.org/abs/2111.11665))

#### Data Embellishment
1. Improving fairness in image classification via sketching. NeurIPS Workshop, 2022. ([paper](https://openreview.net/forum?id=Rq2vt3tnAK9), [code](https://github.com/ubc-tea/Improving-Fairness-in-Image-Classification-via-Sketching))
2. Fairness of classifiers across skin tones in dermatology. MICCAI, 2020. ([paper](https://www.springerprofessional.de/en/fairness-of-classifiers-across-skin-tones-in-dermatology/18443500))

---
### Unfairness Mitigation via In-processing Methods
#### Representation Learning
Training confounder-free deep learning models for medical applications. Nat. Com, 2020. ([paper](https://pubmed.ncbi.nlm.nih.gov/33243992/))
1. Representation learning with statistical independence to mitigate bias. WACV, 2021. ([paper](https://openaccess.thecvf.com/content/WACV2021/papers/Adeli_Representation_Learning_With_Statistical_Independence_to_Mitigate_Bias_WACV_2021_paper.pdf))
2. Risk of training diagnostic algorithms on data with demographic bias. IAELMIC, 2020. Springer ([paper](https://dl.acm.org/doi/abs/10.1007/978-3-030-61166-8_20))
3. Estimating and improving fairness with adversarial learning. ArXiv, 2021. ([paper](https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning))
4. Technical challenges for training fair neural networks. ArXiv, 2021. ([paper](https://arxiv.org/pdf/2102.06764))

#### Disentanglement Learning
1. On the fairness of privacy-preserving representations in medical applications. MICCAI-DART, 2020. ([paper](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170))
2. On fairness of medical image classification with multiple sensitive attributes via learning orthogonal representations. IPMI, 2023. ([paper](https://arxiv.org/pdf/2301.01481))
3. CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions. ECCV-ISIC Workshop, 2022. ([paper](https://link.springer.com/chapter/10.1007/978-3-031-25069-9_14), [code](https://github.com/sfu-mial/CIRCLe))

#### Contrastive Learning
1. FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning. ECCVW, 2022. ([paper](https://arxiv.org/pdf/2208.10013), [code](https://github.com/siyi-wind/FairDisCo))

#### Universal Learning
1. FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification. ArXiv, 2023. ([paper](https://arxiv.org/pdf/2303.08325))

#### Federated Learning
1. On the fairness of swarm learning in skin lesion classification. MICCAI Workshop, 2021. ([paper](https://link.springer.com/chapter/10.1007/978-3-030-90874-4_12))

### Unfairness Mitigation via Post-processing Methods
#### Network Pruning
1. Fairprune: Achieving fairness through pruning for dermatological disease diagnosis. MICCAI, 2022. ([paper](https://link.springer.com/chapter/10.1007/978-3-031-16431-6_70))

---
## Medical Datasets with Sensitive Attributes

## MISC
