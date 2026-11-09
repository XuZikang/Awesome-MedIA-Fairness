# 影像模态标签迁移核查 · 2026-11-09

将主目录中的宽泛Medical imaging拆为有证据支持的具体模态。一个研究可有多个模态；优先使用原始题名、现有已核对摘要和条目中的明确表述。没有模态词的神经影像／视网膜／皮肤病题名不自动推断为MRI／OCT／皮肤镜。

Medical imaging (modality unspecified)表示现有证据不足以指定模态，或文献讨论跨影像场景，不能当作单一模态实证研究。此表不是重新完成所有论文的全文审阅。

| 原始文献 | Domain values | 支持范围 |
|---|---|---|
| [Fairness-related performance and explainability effects in deep learning models for brain image analysis](https://doi.org/10.1117/1.jmi.9.6.061102) | MRI | 综述Table 2 CR1：Brain MRI / ABCD |
| [How fair is your graph? exploring fairness concerns in neuroimaging studies](https://proceedings.mlr.press/v182/ribeiro22a.html) | MRI | 综述Table 2 CR7：Brain MRI / ABIDE |
| [Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations](https://doi.org/10.1038/s41591-021-01595-0) | X-ray | 综述Table 2 CR2：Chest X-ray / MIMIC-CXR, CheXpert, ChestXray14 |
| [Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation](https://doi.org/10.3389/fcvm.2022.859310) | MRI | 综述Table 2 CR4：Heart MRI / UK Biobank |
| [Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis](https://doi.org/10.1073/pnas.1919012117) | X-ray | 综述Table 2 CR13：Chest X-ray / NIH Chest-XRay14, CheXpert |
| [Algorithmic encoding of protected characteristics in image-based models for disease detection](https://arxiv.org/abs/2110.14755) | X-ray | X-ray：X-ray |
| [Feature Robustness and Sex Differences in Medical Imaging: A Case Study in MRI-Based Alzheimer’s Disease Detection](https://doi.org/10.1007/978-3-031-16431-6_9) | MRI | 综述Table 2 CR9：Brain MRI / ADNI |
| [Fairness of Classifiers Across Skin Tones in Dermatology](https://doi.org/10.1007/978-3-030-59725-2_31) | Dermoscopy | 综述Table 2 CR47：Dermatology / ISIC, SD-198 |
| [Improving the Fairness of Chest X-ray Classifiers](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf) | X-ray | 综述Table 2 CR54：Chest X-ray / CheXpert, MIMIC-CXR |
| [MEDFAIR: Benchmarking Fairness for Medical Imaging](https://arxiv.org/abs/2210.01725) | X-ray, MRI, CT, OCT, Fundus photography, Dermoscopy, Clinical photography | [作者仓库Dataset表](https://github.com/ys-zong/MEDFAIR#dataset)：CheXpert/MIMIC-CXR、ADNI、COVID-CT-MD、OCT、PAPILA、HAM10000和Fitzpatrick17k |
| [Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification](https://arxiv.org/abs/2202.02832) | Dermoscopy | 综述Table 2 CR75：Dermatology / ISIC |
| [Evaluating subgroup disparity using epistemic uncertainty in mammography](https://arxiv.org/abs/2107.02716) | Mammography | 综述Table 2 CR60：Mammography / DMIST |
| [Model Selection's Disparate Impact in Real-World Deep Learning Applications](https://arxiv.org/abs/2104.00606) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Harvard Glaucoma Fairness: A Retinal Nerve Disease Dataset for Fairness Learning and Fair Identity Normalization](https://arxiv.org/abs/2306.09264) | OCT | [原文Dataset III-A](https://arxiv.org/html/2306.09264)：OCT扫描及其2D RNFLT投影，不是彩色眼底照片 |
| [Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation](https://doi.org/10.1007/978-3-030-87199-4_39) | MRI | 综述Table 2 CR3：Heart MRI / UK BioBank |
| [Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)](https://doi.org/10.1038/s41467-023-39902-7) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [AI Fairness via Domain Adaptation](https://arxiv.org/abs/2104.01109) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions](https://doi.org/10.1007/978-3-031-25069-9_14) | Clinical photography | 综述Table 2 CR19：Dermatology / Fitzpatrick-17k |
| [CheXclusion: Fairness gaps in deep chest X-ray classifiers](https://pubmed.ncbi.nlm.nih.gov/33691020/) | X-ray | 综述Table 2 CR5：Chest X-ray / MIMIC-CXR, ChestXray8, CheXpert |
| [Improving fairness in image classification via sketching](https://openreview.net/forum?id=Rq2vt3tnAK9) | Dermoscopy | 综述Table 2 CR67：Dermatology / ISIC |
| [Training confounder-free deep learning models for medical applications](https://doi.org/10.1038/s41467-020-19784-9) | CT, MRI, X-ray | 综述Table 2 CR73：Brain MRI, Bone CT / Private dataset |
| [Representation Learning with Statistical Independence to Mitigate Bias](https://doi.org/10.1109/wacv48630.2021.00256) | MRI | 综述Table 2 CR15：Brain MRI / Private dataset |
| [Risk of Training Diagnostic Algorithms on Data with Demographic Bias](https://doi.org/10.1007/978-3-030-61166-8_20) | Dermoscopy | 综述Table 2 CR74：Dermatology / ISIC |
| [Estimating and improving fairness with adversarial learning](https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning) | Dermoscopy | 综述Table 2 CR18：Dermatology / ISIC |
| [Technical Challenges for Training Fair Neural Networks](https://arxiv.org/abs/2102.06764) | X-ray | 综述Table 2 CR10：Chest X-ray / CheXpert |
| [On the fairness of privacy-preserving representations in medical applications](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations](https://arxiv.org/abs/2301.01481) | X-ray | 综述Table 2 CR17：Chest X-ray / CheXpert |
| [FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning](https://arxiv.org/abs/2208.10013) | Clinical photography | 综述Table 2 CR87：Dermatology / Fitzpatrick-17k, Stanford DDI |
| [FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification](https://arxiv.org/abs/2303.08325) | Clinical photography, Dermoscopy | 综述Table 2 CR11：Dermatology / Fitzpatrick-17k, ISIC |
| [On the Fairness of Swarm Learning in Skin Lesion Classification](https://doi.org/10.1007/978-3-030-90874-4_12) | Clinical photography, Dermoscopy | 综述Table 2 CR88：Dermatology / ISIC, Fitzpatrick-17k |
| [FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis](https://doi.org/10.1007/978-3-031-16431-6_70) | Clinical photography, Dermoscopy | 综述Table 2 CR90：Dermatology / ISIC, Fitzpatrick-17k |
| [Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods](https://proceedings.mlr.press/v182/marcinkevics22a.html) | X-ray | 综述Table 2 CR79：Chest X-ray / MIMIC-CXR |
| [A Study of Demographic Bias in CNN-Based Brain MR Segmentation](https://doi.org/10.1007/978-3-031-17899-3_2) | MRI | 综述Table 2 CR8：Brain MRI / ADNI |
| [An Investigation into the Impact of Deep Learning Model Choice on Sex and Race Bias in Cardiac MR Segmentation](https://doi.org/10.1007/978-3-031-45249-9_21) | MRI | 综述Table 2 CR52：Brain MRI / UK BioBank |
| [Revisiting skin tone fairness in dermatological lesion classification](https://doi.org/10.1007/978-3-031-45249-9_24) | Dermoscopy | 综述Table 2 CR48：Dermatology / ISIC |
| [Algorithmic encoding of protected characteristics in chest X-ray disease detection models](https://doi.org/10.1016/j.ebiom.2023.104467) | X-ray | 综述Table 2 CR6：Chest X-ray / CheXpert, MIMIC-CXR |
| [Algorithmic Fairness of Machine Learning Models for Alzheimer Disease Progression](https://doi.org/10.1001/jamanetworkopen.2023.42203) | MRI, PET | 综述Table 2 CR41：Brain MRI / ADNI |
| [An Investigation into Race Bias in Random Forest Models Based on Breast DCE-MRI Derived Radiomics Features](https://doi.org/10.1007/978-3-031-45249-9_22) | MRI | 综述Table 2 CR44：Breast MRI / TCIA |
| [Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease](https://doi.org/10.1007/978-3-031-45249-9_17) | MRI | 综述Table 2 CR42：Brain MRI / ADNI |
| [From Head and Neck Tumour and Lymph Node Segmentation to Survival Prediction on PET/CT: An End-to-End Framework Featuring Uncertainty, Fairness, and Multi-Region Multi-Modal Radiomics](https://doi.org/10.3390/cancers15071932) | CT, PET | 综述Table 2 CR46：PET/CT / HECKTOR |
| [Higher performance for women than men in MRI-based Alzheimer’s disease detection](https://doi.org/10.1186/s13195-023-01225-6) | MRI | 综述Table 2 CR43：Brain MRI / ADNI |
| [Visualizing chest X-ray dataset biases using GANs](https://openreview.net/forum?id=bFb3V8ALx4W) | X-ray | 综述Table 2 CR120：Chest X-ray / CheXpert |
| [The role of subgroup separability in group-fair medical image classification](https://doi.org/10.1007/978-3-031-43898-1_18) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Are sex-based physiological differences the cause of gender bias for chest X-ray diagnosis?](https://doi.org/10.1007/978-3-031-45249-9_14) | X-ray | 综述Table 2 CR59：Chest X-ray / NIH ChestX-ray8, CheXpert |
| [Bias in unsupervised anomaly detection in brain MRI](https://doi.org/10.1007/978-3-031-45249-9_12) | MRI | 综述Table 2 CR40：Brain MRI / ADNI |
| [Detecting shortcuts in medical images-a case study in chest x-rays](https://doi.org/10.1109/isbi53787.2023.10230572) | X-ray | 综述Table 2 CR57：Chest X-ray / CheXpert, NIH ChestX-ray 14 |
| [Evaluating the fairness of deep learning uncertainty estimates in medical image analysis](https://proceedings.mlr.press/v227/mehta24a.html) | Dermoscopy | 综述Table 2 CR12：Multiple / ISIC, BraTS, ADAS13 |
| [A comparative study of fairness in medical machine learning](https://doi.org/10.1109/isbi53787.2023.10230368) | Clinical photography, X-ray | 综述Table 2 CR61：Chest X-ray, Dermatology / JSRT, Stanford DDI |
| [(De) Constructing bias on skin lesion datasets](https://doi.org/10.1109/cvprw.2019.00335) | Dermoscopy | 综述Table 2 CR62：Dermatology / ISIC |
| [Debiasing skin lesion datasets and models? Not so fast](https://doi.org/10.1109/cvprw50498.2020.00378) | Dermoscopy | 综述Table 2 CR63：Dermatology / ISIC |
| [Detect and correct bias in multi-site neuroimaging datasets](https://doi.org/10.1016/j.media.2020.101879) | MRI | 综述Table 2 CR65：Brain MRI / Multi-site MRI |
| [De-identification and obfuscation of gender attributes from retinal scans](https://doi.org/10.1007/978-3-031-45249-9_9) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [EdgeMixup: embarrassingly simple data alteration to improve Lyme disease lesion segmentation and diagnosis fairness](https://doi.org/10.1007/978-3-031-43901-8_36) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Bias in machine learning models can be significantly mitigated by careful training: Evidence from neuroimaging studies](https://doi.org/10.1073/pnas.2211613120) | MRI | 综述Table 2 CR68：Brain MRI / iSTAGING, PHENOM, ABIDE |
| [Addressing Artificial Intelligence Bias in Retinal Diagnostics](https://doi.org/10.1167/tvst.10.2.13) | Fundus photography | Fundus photography：fundus |
| [Equitable modelling of brain imaging by counterfactual augmentation with morphologically constrained 3D deep generative models](https://doi.org/10.1016/j.media.2022.102723) | MRI | 综述Table 2 CR72：Brain MRI / OASIS, UK BioBank |
| [Disproportionate subgroup impacts and other challenges of fairness in artificial intelligence for medical image analysis](https://doi.org/10.1007/978-3-031-23223-7_2) | MRI | 综述Table 2 CR78：Brain MRI / ABCD |
| [A Systematic Review of ‘Fair’ AI Model Development for Image Classification and Prediction](https://doi.org/10.1007/s40846-022-00754-z) | Mammography, X-ray | 综述Table 2 CR77：Chest X-ray, Mammography / Private |
| [Pseudo bias-balanced learning for debiased chest x-ray classification](https://doi.org/10.1007/978-3-031-16452-1_59) | X-ray | 综述Table 2 CR80：Chest X-ray / MIMIC-CXR, ChestXray8 |
| [Rényi fair information bottleneck for image classification](https://arxiv.org/abs/2203.04950) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Improving model fairness in image-based computer-aided diagnosis](https://doi.org/10.1038/s41467-023-41974-4) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Confound removal and normalization in practice: a neuroimaging based sex prediction case study](https://doi.org/10.1007/978-3-030-67670-4_1) | MRI | 综述Table 2 CR85：Brain MRI / HCP |
| [A Penalty Approach for Normalizing Feature Distributions to Build Confounder-Free Models](https://doi.org/10.1007/978-3-031-16437-8_37) | MRI | 综述Table 2 CR84：Brain MRI / USCF, ADNI, SRI |
| [Conditional VAEs for confound removal and normative modelling of neurodegenerative diseases](https://doi.org/10.1007/978-3-031-16431-6_41) | MRI | 综述Table 2 CR86：Brain MRI / UK BioBank, ADNI |
| [Fairness by learning orthogonal disentangled representations](https://arxiv.org/abs/2003.05707) | MRI | 综述Table 2 CR83：Brain MRI / ABIDE |
| [Fairtune: Optimizing parameter efficient fine tuning for fairness in medical image analysis](https://arxiv.org/abs/2310.05055) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Mitigating bias in MRI-based Alzheimer’s disease classifiers through pruning of deep neural networks](https://doi.org/10.1007/978-3-031-45249-9_16) | MRI | 综述Table 2 CR91：Brain MRI / ADNI |
| [Fairness in Deep Learning: A Computational Perspective](https://ieeexplore.ieee.org/document/9113719) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [A Survey on Bias and Fairness in Machine Learning](https://doi.org/10.1145/3457607) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Algorithmic fairness in artificial intelligence for medicine and healthcare](https://doi.org/10.1038/s41551-023-01056-8) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Addressing fairness issues in deep learning-based medical image analysis: a systematic review](https://doi.org/10.1038/s41746-024-01276-5) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Bias recognition and mitigation strategies in artificial intelligence healthcare applications](https://doi.org/10.1038/s41746-025-01503-7) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Algorithmic individual fairness and healthcare: a scoping review](https://doi.org/10.1093/jamiaopen/ooae149) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [The Measure and Mismeasure of Fairness](https://arxiv.org/abs/1808.00023) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Ensuring Fairness in Machine Learning to Advance Health Equity](https://doi.org/10.7326/m18-1990) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Ethical limitations of algorithmic fairness solutions in health care machine learning](https://doi.org/10.1016/s2589-7500(20)30065-0) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Re-imagining Algorithmic Fairness in India and Beyond](https://doi.org/10.1145/3442188.3445896) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Assessing Bias in Medical AI](https://www.cse.cuhk.edu.hk/~qdou/public/IMLH2021_files/64_CameraReady_ICML_2021_Interpretable_Machine_Learning_in_Healthcare_workshop.pdf) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Addressing fairness in artificial intelligence for medical imaging](https://doi.org/10.1038/s41467-022-32186-3) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [The path toward equal performance in medical machine learning](https://doi.org/10.1016/j.patter.2023.100790) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [What's fair is… fair? Presenting JustEFAB, an ethical framework for operationalizing medical ethics and social justice in the integration of clinical machine learning](https://doi.org/10.1145/3593013.3594096) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data](https://doi.org/10.1016/j.ebiom.2024.105501) | MRI | MRI：MRI |
| [Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods](https://doi.org/10.1007/978-3-031-72787-0_1) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation](https://doi.org/10.1093/ehjdh/ztaf008) | MRI | MRI：magnetic resonance |
| [Understanding-informed Bias Mitigation for Fair CMR Segmentation](https://doi.org/10.59275/j.melba.2025-6747) | MRI | MRI：CMR |
| [Shortcut learning in deep neural networks](https://doi.org/10.1038/s42256-020-00257-z) | Other biomedical | 通用医疗公平性／方法背景讨论，不限定影像输入；修正原先宽泛默认影像域，不额外推断模态 |
| [Radiology “forensics”: determination of age and sex from chest radiographs using deep learning](https://doi.org/10.1007/s10140-021-01953-y) | X-ray | X-ray：radiograph |
| [AI recognition of patient race in medical imaging: a modelling study](https://doi.org/10.1016/s2589-7500(22)00063-2) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Implications of predicting race variables from medical images](https://doi.org/10.1126/science.adh4260) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Risk of Bias in Chest Radiography Deep Learning Foundation                     Models](https://doi.org/10.1148/ryai.230060) | X-ray | X-ray：Radiograph |
| [Unveiling Fairness Biases in Deep Learning-Based Brain MRI Reconstruction](https://doi.org/10.1007/978-3-031-45249-9_10) | MRI | MRI：MRI |
| [Disparities in dermatology AI performance on a diverse, curated clinical image set](https://doi.org/10.1126/sciadv.abq6147) | Clinical photography | Clinical photography：clinical image |
| [Understanding skin color bias in deep learning-based skin lesion segmentation](https://doi.org/10.1016/j.cmpb.2024.108044) | Dermoscopy, Clinical photography | Dermoscopy：dermoscop；Clinical photography：clinical images |
| [Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis](https://doi.org/10.1016/j.media.2026.103950) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [A Systematic Study of Race and Sex Bias in CNN-Based Cardiac MR Segmentation](https://doi.org/10.1007/978-3-031-23443-9_22) | MRI | MRI：MR Segmentation |
| [Demographic bias in misdiagnosis by computational pathology models](https://doi.org/10.1038/s41591-024-02885-z) | Histopathology | Histopathology：computational pathology |
| [Unsupervised Bias Discovery in Medical Image Segmentation](https://doi.org/10.1007/978-3-031-45249-9_26) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling](https://arxiv.org/abs/2311.02189) | Scanning laser ophthalmoscopy | [原文Dataset Analysis](https://arxiv.org/html/2311.02189)：SLO fundus为分割输入，OCT提供标注，不混淆输入模态 |
| [Fair AI-powered orthopedic image segmentation: addressing bias and promoting equitable healthcare](https://doi.org/10.1038/s41598-024-66873-6) | X-ray | 原始摘要明确研究plain radiographs；CT/MRI仅为背景介绍，已排除背景词误匹配 |
| [An investigation of race bias in deep learning-based segmentation of prostate MRI images](https://doi.org/10.1038/s41598-025-26189-5) | MRI | MRI：MRI |
| [Diagnosing failures of fairness transfer across distribution shift in real-world medical settings](https://arxiv.org/abs/2202.01034) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Towards Unraveling Calibration Biases in Medical Image Analysis](https://doi.org/10.1007/978-3-031-45249-9_13) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [No Fair Lunch: A Causal Perspective on Dataset Bias in Machine Learning for Medical Imaging](https://arxiv.org/abs/2307.16526) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models](https://arxiv.org/abs/2407.00983) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Editorial Commentary: Calling Balls and Strikes: For Artificial Intelligence Models to Accurately Predict Rotator Cuff Retear, We Must Carefully Define the Strike Zone.](https://pubmed.ncbi.nlm.nih.gov/42701888/) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Responsible AI for Acute Stroke Management.](https://pubmed.ncbi.nlm.nih.gov/42751787/) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Skin color representation in orthopedic literature.](https://pubmed.ncbi.nlm.nih.gov/42975702/) | Medical imaging (modality unspecified) | 题名／可用摘要未明确模态，暂不细分 |
| [Detection and Validation of Hidden Subgroup Disparities in Clinical AI](https://arxiv.org/abs/2610.32362) | X-ray | X-ray：radiograph |
| [Improving the fairness and robustness of deep learning classification models through bias mitigation and post hoc calibration.](https://doi.org/10.1007/s11548-026-03805-x) | MRI | MRI：MRI |
| [Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups](https://arxiv.org/abs/2610.37819) | Clinical photography, X-ray | 原始摘要明确DDI与CheXpert；[DDI官方说明](https://ddi-dataset.github.io/)确认临床皮肤照片 |

## 数据集模态依据

皮肤镜标签仅在题名／摘要明确说明，或综述对应行明确列出ISIC/HAM10000时标注，参见[ISIC官方数据说明](https://challenge.isic-archive.com/data/)。临床皮肤照片参见[Fitzpatrick17k官方说明](https://github.com/mattgroh/fitzpatrick17k)与[DDI官方说明](https://ddi-dataset.github.io/)。数据集映射不表示重新阅读全文。
