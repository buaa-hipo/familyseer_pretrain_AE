#!/bin/bash
# 初始化
source /familyseer_AE/scripts/bashrc_tenset
cd /tenset/scripts
echo $PYTHONPATH
# 本脚本将生成四个log，分别为
# tenset_acc.log（tenset精度）
# tenset_add_acc.log（加入ViT-Huge后的tenset精度）
# family_acc.log（familyseer精度）
# family_add_acc.log（加入ViT-Huge后的familyseer精度）

# tenset数据生成
# =====================================
python make_dataset.py --logs ./dataset/measure_records/t4/*.json --target cuda --sample-in-files 1200 --out-file tenset_dataset.pkl |tee tenset_task.log

# tenset精度测试
# =====================================
# 不可单独运行此步骤，需完成tenset数据生成才可运行
python train_model.py --models xgb --dataset tenset_dataset.pkl|tee /familyseer_AE/scripts/tenset_acc.log

# tenset_add数据生成
# =====================================
python make_dataset.py --logs /flit_file_new/*/*.json --target cuda --out-file tenset_add_dataset.pkl

# tenset_add精度测试
# =====================================
python train_model.py --models xgb --dataset tenset_add_dataset.pkl|tee /familyseer_AE/scripts/tenset_add_acc.log

# family数据生成与精度测试
# =====================================
./make_dataset_split_family.sh
./train_model_split_family.sh|tee /familyseer_AE/scripts/family_acc.log

# family_add数据生成与精度测试
# =====================================
./make_dataset_split_family_add.sh
./train_model_split_family_add.sh|tee /familyseer_AE/scripts/family_add_acc.log
