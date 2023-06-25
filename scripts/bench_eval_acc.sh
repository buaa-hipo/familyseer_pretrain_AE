#!/bin/bash
# will generate four logs
# tenset_acc.log (tenset accuracy)
# tenset_add_acc.log (tenset accuracy after adding ViT-Huge)
# family_acc.log (familyseer accuracy)
# family_add_acc.log（(familyseer accuracy after adding ViT-Huge)

# tenset data
# =====================================
python make_dataset.py --logs ./dataset/measure_records/t4/*.json --target cuda --sample-in-files 1200 --out-file tenset_dataset.pkl |tee tenset_task.log

# tenset test
# =====================================
python train_model.py --models xgb --dataset tenset_dataset.pkl|tee tenset_acc.log

# tenset_add data
# =====================================
python make_dataset.py --logs /flit_file_new/*/*.json --target cuda --out-file tenset_add_dataset.pkl

# tenset_add test
# =====================================
python train_model.py --models xgb --dataset tenset_add_dataset.pkl|tee tenset_add_acc.log

# family
# =====================================
./make_dataset_split_family.sh
./train_model_split_family.sh|tee family_acc.log

# family_add
# =====================================
./make_dataset_split_family_add.sh
./train_model_split_family_add.sh|tee family_add_acc.log
