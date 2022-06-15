import os
dir = "/Users/cjiang/Desktop"

Names = next(os.walk(dir))[1]
TotalNames = len(Names)

TotalSurveys = 0
NameSurveyString = "\n"
for name in Names:
	surveys = len(next(os.walk(dir + "/" + name))[1])
	TotalSurveys += surveys
	NameSurveyString += name + ": " + str(surveys) + "\n"

output = open("output.txt", "w")
output.write("Total Names: " + str(TotalNames) + "\n")
output.write("Total Surveys: " + str(TotalSurveys) + "\n")
output.write(NameSurveyString)