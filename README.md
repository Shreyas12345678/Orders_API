## About the Project

Build an application server with a single API.


<!-- Getting started -->

## Getting Started

### Installation 

1. Fork and Clone
  

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv

    source venv/bin/activate
    ```
   
  

3. Install Flask & Flask-RESTful with pip

    ```bash
    pip install Flask
    pip install flask-restful
    ```


4. Run the server on localhost:
    ```bash
    set FLASK_API=app.py
    flask run
    ```
    
<br>
<br>
## Important Technical Desicion made:
<br>
1. Used Flask as framework to build an rest api using its inbuilt rest_api package.<br>
2. Users are given flexibility to add new items,without any interuption and can change the delivery distance at any time1 <br>
3. User can find Order details and total order cost before confirm the Order<br>
4. Tested the api using Postman(Sreenshots are available in screenshots folder)<br>
    
