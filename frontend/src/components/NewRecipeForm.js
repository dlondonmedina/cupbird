import React, { Component } from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewRecipeForm extends Component {
    state = {
        pk: 0,
        name: "",
        description: "",
        ingredients: [
            {
                name: "",
                qty: 0.0,
                unit: ""
            }
        ],
        procedures: [
            {
                order: 0,
                procedure: ""
            }
        ]
    };

    componentDidMount() {
        if (this.props.recipe) {
            const { pk, name, description, ingredients, procedures } = this.props.recipe;
            this.setState({ pk, name, description, ingredients, procedures });
        }
    }

    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    createRecipe = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    editRecipe = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };

    handleAdd = e => {
        const { target: { name, value } } = e;
        const arr = [...[name]];
        arr.push(value);
        this.setState({[name]: arr});
    }

    handleRemove = e => {
        const { target: { name, value } } = e;
        const arr = [...[name]];
        arr.filter((ingr) => )
    }
    handleAddIngredient = () => {
        this.setState({
            ingredients: this.state.ingredients.concact(
                [
                    { 
                        name: "",
                        qty: 0.0,
                        unit: ""
                    }
                ]
            )
        });
    };

    handleAddProcedure = () => {
        this.setState({
            procedures: this.state.procedures.concact(
                [
                    { 
                        order: this.state.procedures[-1].order + 1,
                        procedure: ""
                    }
                ]
            )
        });
    };

    handleRemove = e => {
        const arr = 
        this.setState({ [e.target.name]: this.state.target.filter})
    };




    render() {
        return (
            <Form onSubmit={this.props.recipe ? this.editRecipe : this.createRecipe}>
                <FormGroup>
                    <Label for="name">Name:</Label>
                    <Input
                        type="text"
                        name="name"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.name)}
                    />
                </FormGroup>
                <FormGroup>
                    <Label for="description">Description:</Label>
                    <Input
                        type="text"
                        name="description"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.description)}
                    />
                </FormGroup>
                <hr />
                
                <Button>Submit</Button>
            </Form>
        );
    }
}

export default NewRecipeForm;
