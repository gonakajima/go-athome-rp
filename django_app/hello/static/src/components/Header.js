import React from 'react';
import Modal from './Modal';

class Header extends React.Component {
  render() {
  　　const headerList = [
  　　  {
  　　    name: 'アカウント作成',
  　　    image: '',
  　　    introduction: 'アカウントを作成します。',
  　　  },
  　　  {
  　　    name: '私の生き方',
  　　    image: '',
  　　    introduction: '',
  　　  },
  　　  {
  　　    name: '事業所を登録',
  　　    image: '',
  　　    introduction: '',
  　　  },
  　　  {
  　　    name: 'ポスト',
  　　    image: '',
  　　    introduction: '',
  　　  },
  　　];

    return (
      <div className='rly_header'>
        <div className='rly_header_inner'>
          <img src='' />
          <h1 className='rbl_txt'>REACTのヘッダー
          </h1>
          //.bl_txt//
          <h2 className='rbl_list'>
            {headerList.map((Item) => {
              return (
                <Mordal
                  name={Item.name}
                  image={Item.image}
                  introduction={Item.introduction}
                />
              );
            })}
          </h2>
          //.rbl_list//
        </div>
        //.rly_header_inner//
      </div>
      //.rly_header//
    );
  }
}

export default Header;