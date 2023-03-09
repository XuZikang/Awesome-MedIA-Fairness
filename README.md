# Awesome-Medical-Image-Analysis-Fairness [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A collection of papers in fairness of medical image analysis

> For more details, please refer to our recent [survey on fairness in medical image analysis](https://arxiv.org/abs/2209.13177)
> 
> Notes: We may miss some relevant papers in the list. If you have any suggestions or would like to add some papers, please submit a pull request or email me at zikangxu@mail.ustc.edu.cn. Your contribution is much appreciated!
---
## Fairness Papers in Medical Image Analysis
### Fairness Evaluation
#### Unfairness Existence
1. Stanley EA, Wilms M, Mouches P, Forkert ND. 2022. Fairness-related performance and explainability effects in deep learning models for brain image analysis. Journal of Medical Imaging 9(6):061102
2. Ribeiro F, Shumovskaia V, Davies T, Ktena I. 2022. How fair is your graph? exploring fairness concerns in neuroimaging studies
3. Seyyed-Kalantari L, Zhang H, McDermott MB, Chen IY, Ghassemi M. 2021. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature medicine 27(12):2176–2182
4. Puyol-Antón E, Ruijsink B, Mariscal Harana J, Piechnik SK, Neubauer S, et al. 2022. Fairness in cardiac magnetic resonance imaging: assessing sex and racial bias in deep learning-based segmentation. Frontiers in Cardiovascular Medicine :664
#### Fairness & Data Distribution
1. Larrazabal AJ, Nieto N, Peterson V, Milone DH, Ferrante E. 2020. Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis. Proceedings of the National Academy of Sciences 117(23):12592–12594
2. Glocker B, Winzeck S. 2021. Algorithmic encoding of protected characteristics and its implications on disparities across subgroups. arXiv preprint arXiv:2110.14755
3. Petersen E, Feragen A, Zemsch LdC, Henriksen A, Christensen OEW, Ganz M. 2022. Feature robustness and sex differences in medical imaging: a case study in mri-based alzheimer’s disease detection. arXiv preprint arXiv:2204.01737
4. Kinyanjui NM, Odonga T, Cintas C, Codella NC, Panda R, et al. 2020. Fairness of classifiers across skin tones in dermatology. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pp. 320–329. Springer
#### Fairness Benchmarking
1. Zhang H, Dullerud N, Roth K, Oakden-Rayner L, Pfohl S, Ghassemi M. 2022. Improving the Fairness of Chest X-ray Classifiers. In Proceedings of the Conference on Health, Inference, and Learning, ed. G Flores, GH Chen, T Pollard, JC Ho, T Naumann, pp. 204–233, vol. 174 of Proceedings of Machine Learning Research, pp. 204–233. PMLR
2. Zong Y, Yang Y, Hospedales T. 2022. Medfair: Benchmarking fairness for medical imaging. arXiv preprint arXiv:2210.01725
#### Fairness & Uncertainty
1. Lu C, Lemay A, Hoebel K, Kalpathy-Cramer J. 2021. Evaluating subgroup disparity using epistemic uncertainty in mammography. arXiv preprint arXiv:2107.02716
#### Fairness & Model Selection
1. Forde JZ, Cooper AF, Kwegyir-Aggrey K, De Sa C, Littman M. 2021. Model selection’s disparate impact in real-world deep learning applications. arXiv preprint arXiv:2104.00606
---
### Unfairness Mitigation via Pre-processing Methods
#### Data Resampling
1. Puyol-Antón E, Ruijsink B, Piechnik SK, Neubauer S, Petersen SE, et al. 2021. Fairness in cardiac mr image analysis: An investigation of bias due to data imbalance in deep learning based segmentation. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pp. 413–423. Springer
2. Brown A, Tomasev N, Freyberg J, Liu Y, Karthikesalingam A, Schrouff J. 2022. Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short). arXiv preprint arXiv:2207.10384
#### Data Synthesis
1. Joshi N, Burlina P. 2021. Ai fairness via domain adaptation. arXiv preprint arXiv:2104.01109
2. Pakzad A, Abhishek K, Hamarneh G. 2022. CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions. In Proceedings of the 17th European Conference on Computer Vision (ECCV) - ISIC Skin Image Analysis Workshop
#### Data Aggregation
1.  Seyyed-Kalantari L, Liu G, McDermott M, Chen IY, Ghassemi M. 2020. CheXclusion: Fairness gaps in deep chest X-ray classifiers. In BIOCOMPUTING 2021: Proceedings of the Pacific Symposium, pp. 232–243. World Scientific
2. Zhou Y, Huang SC, Fries JA, Youssef A, Amrhein TJ, et al. 2021. Radfusion: Benchmarking performance and fairness for multimodal pulmonary embolism detection from ct and ehr. arXiv preprint arXiv:2111.11665
#### Data Embellishment
1. Yao R, Cui Z, Li X, Gu L. 2022. Improving fairness in image classification via sketching. arXiv preprint arXiv:2211.00168
2. Kinyanjui NM, Odonga T, Cintas C, Codella NC, Panda R, et al. 2020. Fairness of classifiers across skin tones in dermatology. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pp. 320–329. Springer
---
### Unfairness Mitigation via In-processing Methods
#### Representation Learning
Zhao Q, Adeli E, Pohl KM. 2020. Training confounder-free deep learning models for medical applications. Nature communications 11(1):1–9
1. Adeli E, Zhao Q, Pfefferbaum A, Sullivan EV, Fei-Fei L, et al. 2021. Representation learning with statistical independence to mitigate bias. In Proceedings of the IEEE/CVF Winter Conference
on Applications of Computer Vision, pp. 2513–2523
2. Abbasi-Sureshjani S, Raumanns R, Michels BE, Schouten G, Cheplygina V. 2020. Risk of training diagnostic algorithms on data with demographic bias. In Interpretable and Annotation-Eﬀicient Learning for Medical Image Computing. Springer
3. Li X, Cui Z, Wu Y, Gu L, Harada T. 2021. Estimating and improving fairness with adversarial learning. arXiv preprint arXiv:2103.04243
4. Cherepanova V, Nanda V, Goldblum M, Dickerson JP, Goldstein T. 2021. Technical challenges for training fair neural networks. arXiv preprint arXiv:2102.06764
#### Disentanglement Learning
1. Sarhan MH, Navab N, Eslami A, Albarqouni S. 2020. On the fairness of privacy-preserving representations in medical applications. In Domain Adaptation and Representation Transfer, and Distributed and Collaborative Learning. Springer
2. Deng W, Zhong Y, Dou Q, Li X. 2023. On fairness of medical image classification with multiple sensitive attributes via learning orthogonal representations. arXiv preprint arXiv:2301.01481
3. Pakzad A, Abhishek K, Hamarneh G. 2022. CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions. In Proceedings of the 17th European Conference on Computer Vision (ECCV) - ISIC Skin Image Analysis Workshop
#### Contrastive Learning
1. Du S, Hers B, Bayasi N, Harmaneh G, Garbi R. 2022. FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning. In Proceedings of the 17th European Conference on Computer Vision Workshops (ECCVW 2022)
#### Universal Learning
#### Federated Learning
1. Fan D, Wu Y, Li X. 2021. On the fairness of swarm learning in skin lesion classification. In Clinical Image-Based Procedures, Distributed and Collaborative Learning, Artificial Intelligence for Combating COVID-19 and Secure and Privacy-Preserving Machine Learning. Springer
### Unfairness Mitigation via Post-processing Methods
#### Network Pruning
1. Wu Y, Zeng D, Xu X, Shi Y, Hu J. 2022. Fairprune: Achieving fairness through pruning for dermatological disease diagnosis. arXiv preprint arXiv:2203.02110
---
## Medical Datasets with Sensitive Attributes

## MISC



<!-- ## New Updates

### Open Source Codes
- [MEDFAIR](https://github.com/ys-zong/MEDFAIR) a benchmarking framework for analyzing fairness in medical images

### Omissive Papers in FAIR-MEDIA

- [Detecting Shortcuts in Medical Images-A Case Study in Chest X-rays](https://arxiv.org/pdf/2211.04279.pdf)
- [Improving Fairness in Image Classification via Sketching (NeurIPS 2022 Workshop)](https://arxiv.org/pdf/2211.00168.pdf)
- [Improving the Fairness of Chest X-ray Classifiers](https://arxiv.org/pdf/2203.12609.pdf)

### Omissive Datasets in FAIR-MEDIA

| Task         |  Name |  Modality  | Body Part | Sensitive Attribute | Link                |
|:------------:|:-----:|:----------:|:---------:|:-------------------:|---------------------|
|Classification|derm7pt| Dermoscope |Skin       |Sex                  |http://derm.cs.sfu.ca|

## Datasets

### Classification
![Classification Datasets with Sensitive Attributes](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/classification.png)

### Segmentation
![Segmentation Datasets with Sensitive Attributes](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/segmentation.png)

### Detection
![Detection Datasets with Sensitive Attributes](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/detection.png)

## Algorithms
![Algorithms](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/algorithm.png)
 -->
