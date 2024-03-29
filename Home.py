<!DOCTYPE html>
<!-- saved from url=(0026)http://localhost:8888/tree -->
<html lang="tr-tr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Home</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./Home_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./Home_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="./Home_files/style.min.css" type="text/css">
    
    <link rel="stylesheet" href="./Home_files/custom.css" type="text/css">
    <script src="./Home_files/promise.min.js.indir" type="text/javascript" charset="utf-8"></script>
    <script src="./Home_files/index.js.indir" type="text/javascript"></script>
    <script src="./Home_files/index.js(1).indir" type="text/javascript"></script>
    <script src="./Home_files/index.js(2).indir" type="text/javascript"></script>
    <script src="./Home_files/require.js.indir" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20221103222346",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./Home_files/contents.js.indir"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./Home_files/custom.js.indir"></script></head>

<body class="" data-jupyter-api-token="059529f7839433083dad8451deded34897d5b71cd9193bec" data-base-url="/" data-notebook-path="" data-terminals-available="True" data-server-root="C:\Users\İrem" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=059529f7839433083dad8451deded34897d5b71cd9193bec" title="dashboard">
      <img src="./Home_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  
  <span class="flex-spacer"></span>
  
    <span id="shutdown_widget">
      <button id="shutdown" class="btn btn-sm navbar-btn" title="Stop the Jupyter server">
          Quit
      </button>
    </span>
  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site" style="height: 647px; display: block;">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="http://localhost:8888/tree#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="http://localhost:8888/tree#running" data-toggle="tab">Running</a></li>
        <li><a href="http://localhost:8888/tree#clusters" data-toggle="tab" class="clusters_tab_link">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions" style="display: none;">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" aria-label="Duplicate selected" class="duplicate-button btn btn-default btn-xs" style="display: inline-block;">Duplicate</button>
                  <button title="Rename selected" aria-label="Rename selected" class="rename-button btn btn-default btn-xs" style="display: none;">Rename</button>
                  <button title="Move selected" aria-label="Move selected" class="move-button btn btn-default btn-xs" style="display: none;">Move</button>
                  <button title="Download selected" aria-label="Download selected" class="download-button btn btn-default btn-xs" style="display: none;">Download</button>
                  <button title="Shutdown selected notebook(s)" aria-label="Shutdown selected notebook(s)" class="shutdown-button btn btn-default btn-xs btn-warning" style="display: inline-block;">Shutdown</button>
                  <button title="View selected" aria-label="View selected" class="view-button btn btn-default btn-xs" style="display: inline-block;">View</button>
                  <button title="Edit selected" aria-label="Edit selected" class="edit-button btn btn-default btn-xs" style="display: inline-block;">Edit</button>
                  <button title="Delete selected" aria-label="Delete selected" class="delete-button btn btn-default btn-xs btn-danger" style="display: inline-block;"><i class="fa fa-trash"></i></button>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id="alternate_upload" class="alternate_upload">
                  <span id="notebook_list_info" class="toolbar_info">
                  <span class="btn btn-xs btn-default btn-upload">
                  <input title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple="multiple">
                  Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu">
                    <li role="presentation" class="dropdown-header" id="notebook-kernels">Notebook:</li><li id="kernel-python3"><a href="http://localhost:8888/tree#" title="Create a new notebook with Python 3">Python 3</a></li>
                    <li role="presentation" class="divider"></li>
                    <li role="presentation" class="dropdown-header">Other:</li>
                    <li role="presentation" id="new-file">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Text File</a>
                    </li>
                    <li role="presentation" id="new-folder">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Folder</a>
                    </li>
                    
                    <li role="presentation" id="new-terminal">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Terminal</a>
                    </li>
                    
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" aria-label="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list" class="list_container">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" aria-label="Select All / None" type="button" class="btn btn-default btn-xs" id="button-select-all">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all"><span id="counter-select-all">1</span>
                </button>
                <button title="Select..." class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id="selector-menu" class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="presentation"><a id="select-folders" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i> Folders</a></li>
                  <li role="presentation"><a id="select-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i> All Notebooks</a></li>
                  <li role="presentation"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i> Running</a></li>
                  <li role="presentation"><a id="select-files" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i> Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb"><li><a href="http://localhost:8888/tree"><i class="fa fa-folder"></i></a></li><li><a href="http://localhost:8888/tree"></a></li></ul>
              </div>
              <div id="file_size" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="file-size">
                      File size
                      <i class="fa"></i>
                  </span>
              </div>
              <div id="last_modified" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="last-modified">
                      Last Modified
                      <i class="fa"></i>
                  </span>
              </div>
              <div id="sort_name" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="sort-name">
                      Name
                      <i class="fa fa-arrow-down"></i>
                  </span>
              </div>
            </div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/3D%20Objects"><span class="item_name">3D Objects</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-01-10 18:54">2 yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/android%2C"><span class="item_name">android,</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-12-29 00:26">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Araba%20oyunu"><span class="item_name">Araba oyunu</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-07-21 10:28">3 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Camera"><span class="item_name">Camera</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-07-28 15:42">3 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Captures"><span class="item_name">Captures</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-10-23 21:14">11 gün önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Contacts"><span class="item_name">Contacts</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Desktop"><span class="item_name">Desktop</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-10-31 14:20">3 gün önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Documents"><span class="item_name">Documents</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-10-13 20:39">21 gün önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Downloads"><span class="item_name">Downloads</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-11-02 14:10">bir gün önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/eclipse"><span class="item_name">eclipse</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-07-21 15:40">3 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/eclipse-workspace"><span class="item_name">eclipse-workspace</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-07-26 15:03">3 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Favorites"><span class="item_name">Favorites</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/ireeem"><span class="item_name">ireeem</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-10-30 20:46">3 yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/%C4%B0%C4%B0"><span class="item_name">İİ</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-12-28 02:10">3 yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Links"><span class="item_name">Links</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/MediaGet2"><span class="item_name">MediaGet2</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-06-30 01:41">4 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Music"><span class="item_name">Music</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/My%20project"><span class="item_name">My project</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-06-25 13:36">4 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/OneDrive"><span class="item_name">OneDrive</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-12-05 15:04">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Pictures"><span class="item_name">Pictures</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-07-01 17:33">4 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Saved%20Games"><span class="item_name">Saved Games</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Searches"><span class="item_name">Searches</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-11-20 19:47">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Source"><span class="item_name">Source</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-10-27 01:14">3 yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/StudioProjects"><span class="item_name">StudioProjects</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2021-12-29 01:02">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Untitled%20Folder"><span class="item_name">Untitled Folder</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-11-03 22:25">24 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Videos"><span class="item_name">Videos</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-06-22 21:59">4 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled.ipynb" target="_blank"><span class="item_name">Untitled.ipynb</span></a><span class="file_size pull-right">1.51 kB</span><span class="item_modified pull-right" title="2022-11-03 22:45">5 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled1.ipynb" target="_blank"><span class="item_name">Untitled1.ipynb</span></a><span class="file_size pull-right">1.64 kB</span><span class="item_modified pull-right" title="2022-11-03 22:40">9 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/Makefile.win" target="_blank"><span class="item_name">Makefile.win</span></a><span class="file_size pull-right">1.17 kB</span><span class="item_modified pull-right" title="2021-12-21 00:33">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/staj%20resimlerii1.docx" target="_blank"><span class="item_name">staj resimlerii1.docx</span></a><span class="file_size pull-right">11.6 kB</span><span class="item_modified pull-right" title="2021-10-21 13:58">bir yıl önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/untitled" target="_blank"><span class="item_name">untitled</span></a><span class="file_size pull-right">0 B</span><span class="item_modified pull-right" title="2022-11-03 22:25">25 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/Untitled-2.c" target="_blank"><span class="item_name">Untitled-2.c</span></a><span class="file_size pull-right">455 B</span><span class="item_modified pull-right" title="2022-01-14 17:49">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/untitled.txt" target="_blank"><span class="item_name">untitled.txt</span></a><span class="file_size pull-right">0 B</span><span class="item_modified pull-right" title="2022-11-03 22:25">25 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/untitled1" target="_blank"><span class="item_name">untitled1</span></a><span class="file_size pull-right">0 B</span><span class="item_modified pull-right" title="2022-11-03 22:25">24 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/untitled1.txt" target="_blank"><span class="item_name">untitled1.txt</span></a><span class="file_size pull-right">0 B</span><span class="item_modified pull-right" title="2022-11-03 22:25">25 dakika önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/%C3%8Ddev11.exe" target="_blank"><span class="item_name">Ídev11.exe</span></a><span class="file_size pull-right">132 kB</span><span class="item_modified pull-right" title="2021-12-21 00:33">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/%C3%96dev11.layout" target="_blank"><span class="item_name">Ödev11.layout</span></a><span class="file_size pull-right">93 B</span><span class="item_modified pull-right" title="2021-12-21 00:38">10 ay önce</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info" class="toolbar_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right toolbar_buttons">
              <button id="refresh_running_list" title="Refresh running list" aria-label="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="http://localhost:8888/tree#">
                  Terminals
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list" class="list_container">
                    <div id="terminal_list_header" class="row list_placeholder" style="display: none;">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  <div class="list_item row"><div class="col-md-12"><i class="item_icon fa fa-terminal"></i><a class="item_link" href="http://localhost:8888/terminals/1" target="_blank"><span class="item_name">terminals/1</span></a><span class="file_size pull-right"></span><span class="item_modified pull-right"></span><div class="item_buttons pull-right"><button class="btn btn-xs btn-warning">Shutdown</button></div></div></div><div class="list_item row"><div class="col-md-12"><i class="item_icon fa fa-terminal"></i><a class="item_link" href="http://localhost:8888/terminals/2" target="_blank"><span class="item_name">terminals/2</span></a><span class="file_size pull-right"></span><span class="item_modified pull-right"></span><div class="item_buttons pull-right"><button class="btn btn-xs btn-warning">Shutdown</button></div></div></div></div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="http://localhost:8888/tree#">
                  Notebooks
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list" class="list_container">
                    <div id="running_list_placeholder" class="row list_placeholder" style="display: none;">
                      <div> There are no notebooks running. </div>
                    </div>
                  <div class="list_item row"><div class="col-md-12"><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled.ipynb" target="_blank"><span class="item_name">Untitled.ipynb</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-11-03 22:49">birkaç saniye önce</span><div class="item_buttons pull-right"><div class="kernel-name">Python 3</div><button class="btn btn-warning btn-xs">Shutdown</button></div></div></div><div class="list_item row"><div class="col-md-12"><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled1.ipynb" target="_blank"><span class="item_name">Untitled1.ipynb</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2022-11-03 22:49">birkaç saniye önce</span><div class="item_buttons pull-right"><div class="kernel-name">Python 3</div><button class="btn btn-warning btn-xs">Shutdown</button></div></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="clusters" class="tab-pane">
          Clusters tab is now provided by IPython parallel.
          See '<a href="https://github.com/ipython/ipyparallel">IPython parallel</a>' for installation details.
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content -->
  </div><!-- ipython-main-app  -->


</div>





    



<script src="./Home_files/main.min.js.indir" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>