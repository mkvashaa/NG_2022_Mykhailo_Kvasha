seconds = int(input("Input seconds: "))
minutes = seconds // 60
seconds_remains = seconds % 60
hours = minutes // 60
minutes_remains = minutes % 60
days = hours // 24
hours_remains = hours % 24
print("Result:", days,"Days", hours_remains,"Hours", minutes_remains,"Minutes", seconds_remains,"Seconds")