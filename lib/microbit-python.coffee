spawn = require('child_process').spawn
path = require('path')
{CompositeDisposable} = require 'atom'

module.exports = MicrobitPython =
  microbitPythonView: null
  modalPanel: null
  subscriptions: null

  activate: (state) ->

    @notificationManager = atom.notifications

    # Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    @subscriptions = new CompositeDisposable

    # Register command that toggles this view
    @subscriptions.add atom.commands.add 'atom-workspace', 'microbit-python:compile': => @compile()
    @subscriptions.add atom.commands.add 'atom-workspace', 'microbit-python:flash': => @flash()

    @pythonpath = 'python'
    @scriptpath = __dirname + '/microbit-python.py'

  deactivate: ->
    @subscriptions.dispose()

  compile: ->
    editor = atom.workspace.getActiveTextEditor()
    fpath = editor.getPath()
    dpath = path.dirname(fpath)
    cmd = spawn(@pythonpath, [@scriptpath, fpath, dpath])
    result = ''
    cmd.stdout.on('data', (data) ->
      result += data.toString()
      )
    nm = @notificationManager
    cmd.on('close', (code) ->
      nm.addInfo(result)
      )

  flash: ->
    editor = atom.workspace.getActiveTextEditor()
    fpath = editor.getPath()
    cmd = spawn(@pythonpath, [@scriptpath, fpath])
    result = ''
    cmd.stdout.on('data', (data) ->
      result += data.toString()
      )
    nm = @notificationManager
    cmd.on('close', (code) ->
      nm.addInfo(result)
      )
