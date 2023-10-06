
echo "BUILD START"
python3.11.6 -m pip install -r requirement.txt 
python3.11.6 manage.py collectstatic --noinput --clear
echo "BUILD END"
