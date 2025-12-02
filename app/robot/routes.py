from flask import Blueprint, render_template, request, redirect, url_for

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/')
def index():
    return "robot"
