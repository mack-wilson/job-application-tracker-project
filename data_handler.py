# data_handler.py
import csv
import os

def load_job_applications(file_name):
    job_applications = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_applications.append(row)
    return job_applications

def add_job_application(file_name, application_data):
    fieldnames = ['job_title', 'company', 'source', 'job_link', 'salary_estimate']
    with open(file_name, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(application_data)

def update_job_application(file_name, application_data, index):
    job_applications = load_job_applications(file_name)
    job_applications[index] = application_data

    fieldnames = ['job_title', 'company', 'source', 'job_link', 'salary_estimate']
    with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for app_data in job_applications:
            writer.writerow(app_data)

def delete_job_application(file_name, index):
    job_applications = load_job_applications(file_name)
    del job_applications[index]

    fieldnames = ['job_title', 'company', 'source', 'job_link', 'salary_estimate']
    with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for app_data in job_applications:
            writer.writerow(app_data)
