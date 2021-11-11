#Wakif Ferdous
#1770041

class Team:
    def __init__(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


student_team= Team()
Teamname= str(input())
teamwins= float(input())
teamlosses= float(input())
student_team.teamname=Teamname
student_team.team_wins=teamwins
student_team.team_losses=teamlosses

if student_team.get_win_percentage() >= 0.50:
    print('Congratulations, Team',student_team.teamname,'has a winning average!')
else:
    print('Team',student_team.teamname, 'has a losing average.')

