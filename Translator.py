#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython import get_ipython


# In[5]:


from IPython.terminal.interactiveshell import TerminalInteractiveShell

#shell = TerminalInteractiveShell.instance()
#shell.define_macro('foo', """a,b=10,20""")
#ipy.embed(display_banner=False)


# In[1]:


get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[1]:


from googletrans import Translator


# In[3]:


def mapper(text):
    translations = {}
    i=0
    for element in text:
        translations[element] = translator.translate(element).text
        i = i+1
        print(i)
    return translations


# In[ ]:




