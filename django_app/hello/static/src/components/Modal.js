import React from 'react';

class Modal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isModalOpen: false};
  }

  handleClickOpen() {
    this.setState({isModalOpen: true});
  }

  handleClickClose(){
    this.setState({isModalOpen: false});
  }

  render() {
    let modal;
    if (this.state.isModalOpen) {
      modal = (
        <div className='rly_modal'>
          <div className='rly_modal_inner'>
            <div className='rly_modal_header'></div>
            <div className='rly_modal_intro'>
              <h2>{this.props.name}</h2>
              <p>{this.props.introduction}</p>
            </div>
            <button
              className='bl_modal_closeBtn'
              onClick={()=>{this.handleClickClose()}}
            >
              とじる
            </button>
          </div>
        </div>
      );
    }

    return (
      <div className='rly_modalOpen_card'>
        <div
          className='rly_modalOpen_item'
          onClick={() => {this.handleClickOpen()}}
        >
          <p>{this.props.name}</p>
          <img src={this.props.image} />
          <p>{this.props.introduction}</p>
        </div>
        {modal}
      </div>
    );
  }
}

export default Modal;