///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* bSizer10;
	bSizer10 = new wxBoxSizer( wxHORIZONTAL );

	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("IP"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	bSizer10->Add( m_staticText3, 0, wxALL, 5 );

	ip = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer10->Add( ip, 1, wxALL, 5 );

	m_staticText4 = new wxStaticText( this, wxID_ANY, wxT("端口号"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4->Wrap( -1 );
	bSizer10->Add( m_staticText4, 0, wxALL, 5 );

	port = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer10->Add( port, 1, wxALL, 5 );

	enter = new wxButton( this, wxID_ANY, wxT("进入"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer10->Add( enter, 1, wxALL, 5 );


	bSizer4->Add( bSizer10, 1, wxEXPAND, 5 );


	bSizer1->Add( bSizer4, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxHORIZONTAL );

	chat = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer7->Add( chat, 0, wxALL, 5 );


	bSizer1->Add( bSizer7, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer9;
	bSizer9 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer13;
	bSizer13 = new wxBoxSizer( wxVERTICAL );

	send1 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer13->Add( send1, 1, wxALL, 5 );


	bSizer9->Add( bSizer13, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer14;
	bSizer14 = new wxBoxSizer( wxVERTICAL );

	send = new wxButton( this, wxID_ANY, wxT("发送"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer14->Add( send, 0, wxALL|wxALIGN_RIGHT, 5 );

	exit = new wxButton( this, wxID_ANY, wxT("退出"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer14->Add( exit, 0, wxALL|wxALIGN_RIGHT, 5 );


	bSizer9->Add( bSizer14, 1, wxEXPAND, 5 );


	bSizer1->Add( bSizer9, 1, wxEXPAND|wxBOTTOM, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}
