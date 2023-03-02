from flask import Blueprint, jsonify, request
from database import db
from user import User
from question import Question
from response import Response
from chat import Chat


user_routes = Blueprint('user_routes', __name__)
que_routes = Blueprint('que_routes', __name__)
resp_routes = Blueprint('resp_routes', __name__)
chat_routes = Blueprint('chat_routes', __name__)



"""User Routes"""
@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'New user created successfully'})

@user_routes.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_routes.route('/user/<string:id>')
def get_user(id):
    usr = User.query.filter_by(id=id).first()
    return jsonify(usr.to_dict())

@user_routes.route('/user_update/<string:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error':'User not found'}), 404
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user.to_dict())

@user_routes.route('/user_delete/<string:id>', methods=['DELETE'])
def delete_user(id):
     usr =  User.query.get(id)
     if usr:
         db.session.delete(usr)
         db.session.commit()
         return jsonify({'message': f'User with id {id} deleted successfully'})
     else:
        return jsonify({'error': f'User with id {id} not found'}), 404

"""Chat Routes"""
@chat_routes.route('/create_chat', methods=['POST'])
def create_chat():
    data = request.json
    chat = Chat(user_id=data['user_id'])
    db.session.add(chat)
    db.session.commit()
    return jsonify({'message': 'New chat created successfully'})

@chat_routes.route('/chats')
def get_chats():
    chats = Chat.query.all()
    return jsonify({'chats': [chat.to_dict() for chat in chats]})

@chat_routes.route('/chat/<string:id>')
def get_chat(id):
    chat = Chat.query.get_or_404(id)
    return jsonify(chat.to_dict())

@chat_routes.route('/chat_update/<string:id>', methods=['PUT'])
def update_chat(id):
    chat = Chat.query.get(id)
    if not chat:
        return jsonify({'error':'Chat not found'}), 404
    data = request.get_json()
    chat.user_id = data['user_id']
    db.session.commit()
    return jsonify(chat.to_dict())

@chat_routes.route('/chat_delete/<string:id>', methods=['DELETE'])
def delete_chat(id):
     c =  Chat.query.get(id)
     if c:
         db.session.delete(c)
         db.session.commit()
         return jsonify({'message': f'Chat with id {id} deleted successfully'})
     else:
        return jsonify({'error': f'Chat with id {id} not found'}), 404
     

"""Response Routes"""
@resp_routes.route('/create_response', methods=['POST'])
def create_response():
    data = request.get_json()
    res = Response(content=data['content'], chat_id=data['chat_id'])
    db.session.add(res)
    db.session.commit()
    return jsonify({'message': 'New response created successfully'})

@resp_routes.route('/responses')
def get_responses():
    res = Response.query.all()
    return jsonify([r.to_dict() for r in res])

@resp_routes.route('/response/<string:id>')
def get_response(id):
    res = Response.query.filter_by(id=id).first()
    return jsonify(res.to_dict())

@resp_routes.route('/response_update/<string:id>', methods=['PUT'])
def update_res(id):
    res = Response.query.get(id)
    if not res:
        return jsonify({'error':'User not found'}), 404
    data = request.get_json()
    res.content = data.get('content', res.content)
    res.chat_id = data.get('chat_id', res.chat_id)
    db.session.commit()
    return jsonify(res.to_dict())

@resp_routes.route('/response_delete/<string:id>', methods=['DELETE'])
def delete_res(id):
     rs =  Response.query.get(id)
     if rs:
         db.session.delete(rs)
         db.session.commit()
         return jsonify({'message': f'User with id {id} deleted successfully'})
     else:
        return jsonify({'error': f'User with id {id} not found'}), 404

"""Question Routes"""
@que_routes.route('/create_question', methods=['POST'])
def new_que():
    data = request.get_json()
    qst = Question(que=data['que'], res_id=data['res_id'])
    db.session.add(qst)
    db.session.commit()
    return jsonify({'message': 'New question created successfully'})

@que_routes.route('/questions', methods=['GET'])
def get_questions():
    que = Question.query.all()
    return jsonify({'questions':[q.to_dict() for q in que]})

@que_routes.route('/question/<string:id>')
def get_question(id):
    que = Question.query.filter_by(id=id).first()
    return jsonify(que.to_dict())

@que_routes.route('/question_update/<string:id>', methods=['PUT'])
def update_question(id):
    q = Question.query.get(id)
    if not q:
        return jsonify({'error':'User not found'}), 404
    data = request.get_json()
    q.que = data.get('que', q.que)
    q.res_id = data.get('res_id', q.res_id)
    db.session.commit()
    return jsonify(q.to_dict())

@que_routes.route('/question_delete/<string:id>', methods=['DELETE'])
def delete_user(id):
     q =  Question.query.get_or_404(id)
     if q:
         db.session.delete(q)
         db.session.commit()
         return jsonify({'message': f'User with id {id} deleted successfully'})
     else:
        return jsonify({'error': f'User with id {id} not found'})



