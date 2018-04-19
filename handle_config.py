# -*- coding: utf-8 -*-

import os, sys
import project_manage, tag_manage, task_manage


f = open('config.ini','r',encoding='utf-8')
while True:
    lines = f.readline()
    if lines:
        print (lines)
        if lines.startswith('Plan:'):
            plan_list = lines.split(' ')
            if plan_list[2] == 'project':
                project = project_manage.Project_manage()
                if plan_list[1] == 'add':
                    project.add_project(plan_list[3], plan_list[4], plan_list[5], plan_list[6])
                elif plan_list[1]  == 'delete':
                    project.delete_project()
                elif plan_list[1] == 'modify':
                    project.modify_project()
                elif plan_list[1] == 'find':
                    project.find_project()
                else:
                    print ('error')
            elif plan_list[2] == 'task':
                task = task_manage.Task_manage
                if plan_list[1] == 'add':
                    task.add_task()
                elif plan_list[1]  == 'delete':
                    task.delete_task()
                elif plan_list[1] == 'modify':
                    task.modify_task()
                elif plan_list[1] == 'find':
                    task.find_task()
                else:
                    print('error')
            elif plan_list[2]  == 'tag':
                tag = task_manage.Task_manage
                if plan_list[1] == 'add':
                    tag.add_task()
                elif plan_list[1]  == 'delete':
                    tag.delete_task()
                elif plan_list[1] == 'modify':
                    tag.modify_task()
                elif plan_list[1] == 'find':
                    tag.find_task()
                else:
                    print('error')
            else:
                print('error')
            for i in range(len(plan_list)):

    else:
        break