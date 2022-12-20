import sqlite3

connectinon = sqlite3.connect("for_typing_test.bd")
cursor = connectinon.cursor()

result = cursor.execute(f"UPDATE results SET ru_result = 385 WHERE user_name='keysiks'")
cursor.execute(f"UPDATE results SET eng_result = 362 WHERE user_name='keysiks'")
connectinon.commit()