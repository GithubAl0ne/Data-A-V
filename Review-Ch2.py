# الفصل الثاني – مراجعة مكتبة pandas (الوحدات 1–4)
# يشمل:
# - Series
# - DataFrame
# - العمليات على Series و DataFrame
# - قراءة CSV
# - دمج DataFrames
# - إعادة الفهرسة، الحذف، الترتيب، التخزين

import pandas as pd
import numpy as np

# -----------------------------
# الوحدة 1: Series
# -----------------------------

# 1) إنشاء Series بفهرس تلقائي
s1 = pd.Series([4, 7, -5, 3])
print("Series s1:\n", s1)

# عرض القيم والفهرس
print("s1.values:", s1.values)
print("s1.index:", s1.index)

# 2) إنشاء Series بفهرس مخصص
s2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print("\nSeries s2:\n", s2)

# الوصول لعناصر وتعديلها
print("قيمة الفهرس 'a' في s2:", s2['a'])
s2['d'] = 6
print("بعد تعديل 'd' في s2:\n", s2)

# فلترة وعمليات
print("\nالعناصر > 0 في s2:\n", s2[s2 > 0])
print("ضرب s2 * 2:\n", s2 * 2)

# 3) Series من قاموس
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s3 = pd.Series(sdata)
print("\nSeries s3 من قاموس:\n", s3)

# التعرف على القيم الفارغة (null)
obj4 = pd.Series({'California': np.nan, 'Ohio': 35000, 'Oregon': 71000, 'Texas': 16000})
print("\nobj4:\n", obj4)
print("isnull(obj4):\n", pd.isnull(obj4))
print("notnull(obj4):\n", pd.notnull(obj4))

# عمليات بين Series (توافق الفهارس)
print("\nجمع s3 + obj4:\n", s3 + obj4)

# -----------------------------
# الوحدة 2: DataFrame
# -----------------------------

# إنشاء DataFrame من قاموس
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
print("\nDataFrame frame:\n", frame)

# تحديد ترتيب الأعمدة
frame_ordered = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print("\nframe_ordered:\n", frame_ordered)

# تحديد الأعمدة والفهرس مع عمود إضافي debt
frame2 = pd.DataFrame(
    data,
    columns=['year', 'state', 'pop', 'debt'],
    index=['one', 'two', 'three', 'four', 'five', 'six']
)
print("\nDataFrame frame2:\n", frame2)

# استرجاع عمود
print("\nعمود state:\n", frame2['state'])
print("\nعمود year:\n", frame2.year)

# استرجاع صف باستخدام loc
print("\nالصف 'three':\n", frame2.loc['three'])

# إضافة عمود debt بقيم متسلسلة
frame2['debt'] = np.arange(6.)
print("\nframe2 بعد إضافة debt:\n", frame2)

# إضافة عمود debt باستخدام Series مع توافق الفهارس
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print("\nframe2 بعد تعيين debt من Series:\n", frame2)

# إنشاء عمود جديد بناءً على عمود state
frame2['eastern'] = frame2.state == 'Ohio'
print("\nframe2 بعد إضافة eastern:\n", frame2)

# حذف عمود eastern
del frame2['eastern']
print("\nالأعمدة بعد حذف eastern:\n", frame2.columns)

# القيم فقط (NumPy array)
print("\nframe2.values:\n", frame2.values)

# -----------------------------
# الوحدة 3: عمليات على pandas – الجزء الأول
# -----------------------------

# مثال DataFrame لإعادة الفهرسة
frame3 = pd.DataFrame(
    np.arange(9).reshape(3, 3),
    index=['a', 'c', 'd'],
    columns=['Ohio', 'Texas', 'California']
)
print("\nframe3:\n", frame3)

# إعادة ترتيب الأعمدة (reindex)
states = ['Texas', 'Utah', 'California']
frame3_reindexed = frame3.reindex(columns=states)
print("\nframe3 بعد reindex للأعمدة:\n", frame3_reindexed)

# حذف عناصر من Series
obj = pd.Series([0., 1., 2., 3., 4.], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries obj:\n", obj)
obj_dropped = obj.drop(['d', 'c'])
print("\nobj بعد حذف 'd' و 'c':\n", obj_dropped)

# حذف صفوف وأعمدة من DataFrame
data_df = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=[0, 1, 2, 3],
    columns=['a', 'b', 'c', 'd']
)
print("\nDataFrame data_df:\n", data_df)

# حذف صفوف
data_rows_dropped = data_df.drop([0, 1])
print("\ndata_df بعد حذف الصفوف 0 و 1:\n", data_rows_dropped)

# حذف أعمدة (axis=1)
data_cols_dropped = data_df.drop('b', axis=1)
print("\ndata_df بعد حذف العمود 'b':\n", data_cols_dropped)

# ترتيب الصفوف أو الأعمدة
sorted_cols = data_df.sort_index(axis=1, ascending=True)
print("\ndata_df بعد sort_index للأعمدة تصاعدي:\n", sorted_cols)

# تطبيق دالة على DataFrame (مثل الضرب في 2)
data_times2 = data_df * 2
print("\ndata_df * 2:\n", data_times2)

# -----------------------------
# الوحدة 4: عمليات على pandas – الجزء الثاني
# -----------------------------

# إنشاء DataFrame يشبه students.csv
students = pd.DataFrame({
    'ID': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Ahmed', 'Mohamed', 'Ali', 'Hassan', 'Hossam', 'Zyad',
             'Fahd', 'Khaled', 'Ali', 'Ahmed', 'Mohamed'],
    'Age': [20, 20, 21, 21, 20, 22, 22, 20, 21, 20, 21]
})
print("\nstudents:\n", students)

# إنشاء DataFrame يشبه marks.csv
marks = pd.DataFrame({
    'ID': [100, 101, 103, 104, 105, 108, 109],
    'Level': [7, 7, 6, 7, 8, 6, 7],
    'Grade': ['A', 'A+', 'B+', 'B+', 'A', 'A+', 'B+']
})
print("\nmarks:\n", marks)

# info و describe
print("\nstudents.info():")
students.info()
print("\nstudents.describe():\n", students.describe())

# استرجاع عمود
print("\nعمود Name من students:\n", students['Name'])

# استرجاع صف و عنصر باستخدام loc
print("\nصف الفهرس 10 في students:\n", students.loc[10])
print("\nالعنصر Name في الصف 10:\n", students.loc[10, 'Name'])

# دمج DataFrames – outer (كل البيانات)
stdf_outer = pd.merge(students, marks, on='ID', how='outer')
print("\nدمج students و marks (outer):\n", stdf_outer)

# دمج DataFrames – inner (البيانات المشتركة فقط)
stdf_inner = pd.merge(students, marks, on='ID', how='inner')
print("\nدمج students و marks (inner):\n", stdf_inner)

# تغيير اسم عمود
students_renamed = students.rename(columns={'ID': 'ID1'})
print("\nstudents بعد إعادة تسمية ID إلى ID1:\n", students_renamed)

# تخزين DataFrame في CSV (افتراضيًا سيُنشئ ملف في نفس المجلد)
# stdf_inner.to_csv('combined.csv', index=False)
# ملاحظة: السطر أعلاه فعّال عند التشغيل الفعلي في بيئة بها نظام ملفات.

print("\nتم تنفيذ جميع الأجزاء من الوحدات 1–4 في كود واحد.")
print("\ntest")