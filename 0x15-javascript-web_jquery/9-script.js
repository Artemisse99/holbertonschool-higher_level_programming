#!/usr/bin/node
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('DIV#hello').append('<li>' + data.hello + '</li>');
});
