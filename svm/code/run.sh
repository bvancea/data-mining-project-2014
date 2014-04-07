echo "Training classifier"
python mapper.py < ../data/training | python reducer.py > weights.txt

echo "Computing accuracy on training data"
python evaluate.py weights.txt ../data/training_features ../data/training_labels