"""Routes for the course resource.
"""

from run import app
from flask import request,jsonify,Response
from http import HTTPStatus
import data
import json

@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    with open('json/course.json','r') as f:
        data = json.load(f)
        message = {"message":"course " +str(id)+ " does not exist"}
        status = 404
        for course in data:
            if course["id"]==id:
                message = course
                status=200


    response = Response(json.dumps(message), status, mimetype='application/json')
    return response



    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['GET'])
def get_courses():
    with open('json/course.json','r') as f:
        titleWords = request.args.get('title-words')
        pageNumber = int(request.args.get('page-number')) if request.args.get('page-number') else None
        pageSize = int(request.args.get('page-size')) if request.args.get('page-size') else None 
        filteredData = []
        data = json.load(f)
        if titleWords:
            newData = []
            for word in titleWords.split(','):
                for item in data:
                    if word in item['title'].lower():
                        if item not in newData:
                            newData.append(item) 
            data = newData
        if pageNumber and pageSize and data:
            for course in range(pageSize*(pageNumber-1), pageNumber*pageSize):
                filteredData.append(data[course])
            if(titleWords):
                for filteredCourse in filteredData:
                    print(filteredCourse['title'])
                    if(titleWords not in filteredCourse['title']):
                        filteredData.remove(filteredCourse)

            return jsonify(filteredData)

    return jsonify(data)


    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['POST'])
def create_course():

    with open('json/course.json','r') as f:
        data = json.load(f)
        data.append(dict(request.args))
    with open('json/course.json','w') as f:
        json.dump(data,f)
    
    status = 201
    message = dict(request.args)

    response = Response(json.dumps(message), status, mimetype='application/json')
    return response


    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    with open('json/course.json','r') as f:
        data = json.load(f)
        message = {"message":"course " +str(id)+ " does not match the payload"}
        status = 404
        for course in data:
            if course["id"]==id:
                for key in dict(request.args):
                    course[key] = dict(request.args)[key]
                message = course
                status=200
    with open('json/course.json','w') as f:
        json.dump(data,f)


    response = Response(json.dumps(message), status, mimetype='application/json')
    return response


    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    with open('json/course.json','r') as f:
        data = json.load(f)
        message = {"message":"course " +str(id)+ " does not exist"}
        status = 404
        for course in data:
            if course["id"]==id:
                data.remove(course)
                message = {"message":"The Specified course was deleted"}
                status=200

    with open('json/course.json','w') as f:
        json.dump(data,f)


    response = Response(json.dumps(message), status, mimetype='application/json')
    return response
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE

