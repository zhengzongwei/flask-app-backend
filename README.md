# flask-app


## 
## 更新model
```python
flask db init
flask db migrate -m "message"
flask db upgrade
```

## 更新翻译
```python
# 生成翻译模版
pybabel extract -F babel.cfg -o messages.pot .

# 创建翻译
pybabel init -i messages.pot -d locale -l zh_CN

# 编译翻译
pybabel compile -d locale


# 更新翻译模版
pybabel update -i messages.pot -d locale

pybabel --list-locales 
```

