#!/usr/bin/python3
"""States module"""

from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/', methods=['GET'])
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states.values()]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a State"""
    data = request.get_json()
    if data is None:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    return (jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, description="Not a JSON")
    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict())
