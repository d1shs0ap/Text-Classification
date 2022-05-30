for dataset in 'AG_NEWS' 'DBpedia' 'SogouNews'
do
for shot in '5shot' '10shot' '50shot' '100shot'
do
for experiment in 1 2 3 4 5
do
python preprocess.py --config kshot/$dataset/$shot/$experiment/fasttext/fasttext.yaml
python train.py --config kshot/$dataset/$shot/$experiment/fasttext/fasttext.yaml
python test.py --config kshot/$dataset/$shot/$experiment/fasttext/fasttext.yaml > kshot/$dataset/$shot/$experiment/fasttext/log.txt
done
done
done
