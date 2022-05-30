for dataset in 'AG_NEWS' 'DBpedia' 'SogouNews'
do
for shot in '5shot' '10shot' '50shot' '100shot'
do
for experiment in 1 2 3 4 5
do
echo $dataset
echo $shot
echo $experiment
cat kshot/$dataset/$shot/$experiment/fasttext/log.txt
done
done
done
