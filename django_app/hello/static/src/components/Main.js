import React from 'react';
import Modal from './Modal';

class Main extends React.Component {
  render() {
    const mainList = [
      {
        name: '往診を申し込む',
        image: '',
        introduction: '',
      },
      {
        name: 'かかりつけ医を探す',
        image: '',
        introduction: '',
      },
      {
        name: 'ケアマネを探す',
        image: '',
        introduction: '',
      },
      {
        name: '施設を探す',
        image: '',
        introduction: '',
      },
    ];

    return (
      <div className='rly_cont'>
        <div className='rly_cont_main'>
          <h1>REACTのメイン</h1>
        </div>
        //.rly_cont_main//
        <div className='rly_cont_col'>
          <div className='rly_cont_modal'>
            {mainList.map((Item) => {
              return (
                <Mordal
                  name={Item.name}
                  image={Item.image}
                  introduction={Item.introduction}
                />
              );
            })}
          </div>
          //.rly_cont_modal//
        </div>
        //.rly_cont_col//
      </div>
      //.rly_cont//
    );
  }
}

export default Main;