# How To run this script in a terminal?

Preparation (after installation of anaconda):
```
pip3 install -r requirements.txt
unzip data.zip
```

Running
```
git pull
rm nohup.out
nohup python3 badenes_terms.py &
```

See results/outputs:
```
tail -f nohup.out (if it is running)
cat nohup.out (if it is stopped)
```
