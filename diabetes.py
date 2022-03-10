import csv
from matplotlib import pyplot as plt
# show_barchart_gender=True


def generate_summary_for_web(csvfile, html_title, html_filename,
                             show_barchart_gender=True):
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = []
        for line in reader:
            data.append(line)

        pcounts_per_column = []
        ncounts_per_column = []
        for e in range(2, 16):
            pcount_yes = 0
            pcount_No = 0
            ncount_yes = 0
            ncount_No = 0
            # missing bottom two columns
            for i in range(520):

                if ("Yes" == data[i][e]) and ("Positive" == data[i][16]):
                    pcount_yes = pcount_yes + 1
                if ("No" == data[i][e]) and ("Positive" == data[i][16]):
                    pcount_No = pcount_No + 1
                if ("Yes" == data[i][e]) and ("Negative" == data[i][16]):
                    ncount_yes = ncount_yes + 1
                if ("No" == data[i][e]) and ("Negative" == data[i][16]):
                    ncount_No = ncount_No + 1
            pcounts_per_column.append(["Yes", pcount_yes])
            pcounts_per_column.append(["No", pcount_No])
            ncounts_per_column.append(["Yes", ncount_yes])
            ncounts_per_column.append(["No", ncount_No])
        File = open(html_filename, "w")
        File.write("<!DOCTYPE html>\n<html>\n<head>\n<Title>")
        File.write(html_title+"\n</Title>\n<style>")
        File.write("\ntable{\nborder: 2px solid black;\n}")
        File.write("\nth{\nborder: 2px solid black;\nbackground-color:")
        File.write("blue;\n}")
        File.write("\ntd {\n font-family:Times New Roman, Times;")
        File.write("\nfont-size:120%;")
        File.write("\nborder: 2px solid black;\n}")
        File.write("\n\t.aligncenter {\ntext-align: center;\n}")
        File.write("\n</style>\n</head>")
        File.write("\n<body>\n<h1 align=center>"+html_title+"\n</h1>")
        File.write("<Table align= center width=400 height = 500>")
        File.write("\n<tr>\n<th rowspan = 3>Attributes</th>")
        File.write("\n<th colspan = 4>Class</th>\n</tr>")
        File.write("\n<tr>\n<th colspan = 2>Postive</th>")
        File.write("\n<th colspan = 2>Negative</th>\n</tr>")
        File.write("\n<tr>\n<th>Yes</th>\n<th>No</th>\n<th>Yes</th>")
        File.write("\n<th>No</th>\n</tr>")

        index = 2
        # learn how to shade table
        # if i is odd number make bar shaded eg
        for i in range(0, 28, 2):
            if(i % 4 == 0):
                File.write("\n<tr style = background-color:#4ca3dd>")
                File.write("\n<td>"+header[index]+"</td>")
                File.write("\n<td>"+str(pcounts_per_column[i][1])+"</td>")
                File.write("\n<td>"+str(pcounts_per_column[i+1][1])+"</td>")
                File.write("\n<td>"+str(ncounts_per_column[i][1])+"</td>")
                File.write("\n<td>"+str(ncounts_per_column[i+1][1])+"</td>")
                File.write("\n<tr>")
                index = index+1
            else:
                File.write("\n<tr style = background-color:#c6e2ff>")
                File.write("\n<td>"+header[index]+"</td>")
                File.write("\n<td>"+str(pcounts_per_column[i][1])+"</td>")
                File.write("\n<td>"+str(pcounts_per_column[i+1][1])+"</td>")
                File.write("\n<td>"+str(ncounts_per_column[i][1])+"</td>")
                File.write("\n<td>"+str(ncounts_per_column[i+1][1])+"</td>")
                File.write("\n<tr>")
                index = index+1

        mcount = []
        fcount = []
        myes = 0
        mno = 0
        fyes = 0
        fno = 0

        if(show_barchart_gender is True):
            for i in range(520):
                if(data[i][1] == "Male") and (data[i][16] == "Positive"):
                    myes = myes + 1
                if(data[i][1] == "Male") and (data[i][16] == "Negative"):
                    mno = mno + 1
                if(data[i][1] == "Female") and (data[i][16] == "Positive"):
                    fyes = fyes + 1
                if(data[i][1] == "Female") and (data[i][16] == "Negative"):
                    fno = fno + 1
            mcount.append(myes)
            mcount.append(mno)
            fcount.append(fyes)
            fcount.append(fno)
            label1 = ["Positive", "Negative"]
            xaxis = [1, 2]
            w = 0.25
            x1 = [i - w/2 for i in xaxis]
            x2 = [i + w/2 for i in xaxis]
            plt.bar(x1, mcount, label="Male", width=w, color="red")
            plt.bar(x2, fcount, label="Female", width=w, color="blue")
            plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y',
                     alpha=0.7)
            plt.xticks(xaxis, label1)
            plt.xlabel("Class")
            plt.ylabel("Count")
            plt.title("Gender of Positive vs Negative cases")
            plt.text(0.82, 150, str(mcount[0]))
            plt.text(1.08, 176, str(fcount[0]))
            plt.text(1.82, 182, str(mcount[1]))
            plt.text(2.08, 21, str(fcount[1]))
            plt.legend(["Male", "Female"], title="Gender",
                       loc="upper right", prop={'size': 8})
            plt.savefig("Graph.png")
            plt.show

            File.write("\n</table>")
            File.write("<p class=aligncenter>\n<img src=Graph.png")
            File.write("\nalt=Graph-for-gender width =800px height = 600px/>")
            File.write("\n</p>")
        File.write("\n</body>\n</html>")
# also makegraphs and table more advanced to get better marks
#  male to female no on postive/ negatiev
