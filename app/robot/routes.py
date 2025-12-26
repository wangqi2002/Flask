from flask import Blueprint, render_template, request, redirect, url_for

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/reply')
def index():
    comment = request.values.get("question")
    print(comment)
    return "这里是机器人提供的答复"

@robot_bp.route('/text')
def index():
    comment = request.values.get("audio")
    print(comment)
    return "这里是语音转文字提供的答复"
