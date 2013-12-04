from django.contrib.auth.decorators import login_required
from competition.models import SchoolStudent, School, Invigilator, Venue 


@login_required
def typeset_details(request):
	""" Formats student information for the particular user """

	username = request.user #Current user
	studentOptions = SchoolStudent.objects.filter(registered_by = username)
					#Gets all the students who were registered by current user

	pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
 	individual_list = { 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}
 
	for student in studentOptions:
		
		if student.firstname == '': # Better pair condition logic for this!
			pair_list[student.grade] += 1
		
		else: #Store individual in grade bin
			individual_list[student.grade].append((student.firstname, student.surname))

	
	output_string = 'Confirmation letter for %s requested by %s\n'%(studentOptions[0].school, username)
   			
	temp_output = open('confirmation.txt', 'w')	
	temp_output.write('' + output_string + print_grade(individual_list, pair_list))
	temp_output.close()	
					

def print_grade(single_list, pair_list):
	""" Prints and formats the data for each grade """

	return_string = ''
	pair_set = ['A','B','C','D','E']
	
	for grade in range(8, 13):	
		grade_string = '\n%s\nGrade %d students (%d registered):\n%s\n'%('-'*40, grade, len(single_list[grade]) + pair_list[grade], '-'*40)
		grade_string+= '\n%-15s %-15s \n%s\n'%('First Name', 'Surname', '- '*20)
		
		for single in single_list[grade]:
			grade_string+= '%-15s %-15s\n'%(single[0], single[1])
		
		grade_string += '\n%d pairs registered\n'%(pair_list[grade]/2) 
		
		for pair_register in range(1, pair_list[grade]/2+1):
			grade_string += 'Group %d: \n %s %s \n %s %s\n'%(pair_register, '_'*12, '_'*12, '_'*12, '_'*12)

		return_string += grade_string + '\n'		

	return return_string #Stored as one long formatted string. 

def UMC_header():
	to_return = '%s\n%s^40\n%s'%('- '*20, 'UCT Maths Competition', '- '*20)
