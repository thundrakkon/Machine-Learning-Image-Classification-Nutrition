from prettytable import PrettyTable
csv_file =open('Final_Fruits_Veggies.csv','r')
csv_file = csv_file.readlines()
line_1 = csv_file[0]
line_1 = line_1.split(',') 
line_2 = csv_file[1]
line_2 = line_2.split(',')       
x = PrettyTable([line_1[0], line_2[0]])
for a in range(1,len(line_1)):
    x.add_row([line_1[a], line_2[a]])
html_code = x.get_html_string()
html_file = open('table.html','w')

html_file = html_file.write(html_code)


