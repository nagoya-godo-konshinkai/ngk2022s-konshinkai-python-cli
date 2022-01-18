# ngk2022s-konshinkai-python-cli
NGK2022Sの懇親会用ツールです

# Requirements
* python3.8+

# Install

```
$ poetry install
```


# Usage

`input.csv`に記載されているユーザを、3個のテーブルに割り当てます。

```
$ poetry run python assign_table.py --input input.csv --table_count 3 --output output.csv
```

### input.csv
GoogleスプレッドシートからCSVをダウンロードします。

```csv
タイムスタンプ,oviceの名前を入力してください。
2022/01/18 16:26:04,name1
2022/01/18 16:26:04,name2
2022/01/18 16:26:04,name3
2022/01/18 16:26:04,name4
2022/01/18 16:26:04,name5
2022/01/18 16:26:04,name6
2022/01/18 16:26:04,name7
2022/01/18 16:26:04,name8
2022/01/18 16:26:04,name9
2022/01/18 16:26:04,name10
```


### output.csv

```csv
user,table_name
name1,C
name10,A
name2,B
name3,C
name4,C
name5,A
name6,B
name7,A
name8,B
name9,A
```
