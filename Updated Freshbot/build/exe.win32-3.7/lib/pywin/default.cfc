�   z00000409�   B
�  �R�_��idle extensions{� [   zFormatParagraphzCallTips0�keys{r   {)�Q   �   z<<format-paragraph>>)�W   �   zViewWhitespace)�8   �   zViewWhitespace)�F   r	   zViewFixedFont)�   r   z<<expand-word>>)�    r   z<<expand-word>>)�9   �   z<<paren-open>>)�0   r   z<<paren-close>>)�&   �    z<<check-calltip-cancel>>)�(   r   z<<check-calltip-cancel>>)�%   r   z<<check-calltip-cancel>>)�'   r   z<<check-calltip-cancel>>)�   r   zKeyDot)�x   r   zDbgBreakpointToggle)�t   r   zDbgGo)r   r   zDbgClose)�z   r   zDbgStep)�y   r   zDbgStepOver)r   r   z
DbgStepOut)�r   r   zAutoFindNext0zeditor{)�q   r   zGotoNextBookmark)r   r   zToggleBookmark)�G   r   zGotoLine)�I   r   zShowInteractiveWindow)�B   r   z	AddBanner)�3   r   z<<comment-region>>)r   �   z<<uncomment-region>>)�4   r   z<<uncomment-region>>)�5   r   z<<tabify-region>>)�6   r   z<<untabify-region>>)�   r   z<<smart-backspace>>)�T   r   z<<toggle-tabs>>)�U   r   z<<change-indentwidth>>)�   r   zEnterKey)�	   r   zTabKey)r(   r   z<<dedent-region>>)�k   r   z
FoldExpand)r)   r   zFoldExpandAll)r)   r   zFoldExpandSecondLevel)�m   r   zFoldCollapse)r*   r   zFoldCollapseAll)r*   r   zFoldCollapseSecondLevel)�j   r   zFoldTopLevel0zinteractive{)r   r   z<<history-previous>>)r   r   z<<history-next>>)r'   r   zProcessEnter)r'   r   zProcessEnter)r'   r   zProcessEnter)�   r   z
ProcessEsc)r   r   z
WindowBack)�$   r   zInteractiveHome)r-   r   zInteractiveHomeExtend)r(   r   zMDINext)r(   r	   zMDIPrev00�extension codec               @   sD   d d� Z dd� Zdd� Zdd� Zdd	� Zd
d� Zdd� Zdd� ZdS )c             C   sn   | j }d}d||f }|�d�}|��  |�||� |��  dd� |�d�D �\}}|�dd|d	 f � d S )
NzF######################################################################z%s
## 
## 
## 
%s
zinsert linestartc             S   s   g | ]}t |��qS � )�int)�.0�sr/   r/   �9C:\python37\lib\site-packages\Pythonwin\pywin\default.cfg�
<listcomp>�   s    zAddBanner.<locals>.<listcomp>�.�insertz%d.1 lineend�   )�text�index�undo_block_startr6   �undo_block_stop�split�mark_set)�editor_window�eventr8   Zbig_line�banner�pos�line�colr/   r/   r3   �	AddBanner�   s    
rD   c             C   s   t | jd�S )Nr   )�_DoInteractiveHomer8   )r>   r?   r/   r/   r3   �InteractiveHome�   s    rF   c             C   s   t | jd�S )N�   )rE   r8   )r>   r?   r/   r/   r3   �InteractiveHomeExtend�   s    rH   c             C   st   dd l }| j�� rdS dt|j� }| �dd|�sP| �d|�|j|jgkrP|}nd}|r^d}n|}| �d||� d S )Nr   rG   zinsert linestart + %d cr6   z==zinsert linestart�sel)	�sys�edit�SCIAutoCActive�len�ps1�compare�get�ps2�tag_add)r8   �extendrJ   Zof_interest�end�startr/   r/   r3   rE   �   s    
 rE   c       
      C   s�   ddl m} ddl m} y|| j}|�� }|rB||j_|�� |j_nP|�	|j
�}|�	|j|d�}|�	|j|d�}|�||�}|r�||j_||f|j_W n$ tk
r�   ddl}	|	��  Y nX |��  dS )z'find selected text or word under cursorr   )�find)�scintillaconrG   N)�pywin.scintillarV   rW   rK   �
GetSelTextZ
lastSearch�findText�GetSelrI   �SendScintilla�SCI_GETCURRENTPOS�SCI_WORDSTARTPOSITION�SCI_WORDENDPOSITION�GetTextRange�	Exception�	traceback�	print_exc�FindNext)
r>   r?   rV   rW   �sci�wordrA   rU   rT   rb   r/   r/   r3   �AutoFindNext�   s&    rg   c             C   s   | j ��  d S )N)r8   Zbeep)r>   r?   r/   r/   r3   �Beep�   s    rh   c             C   s   d S )Nr/   )r>   r?   r/   r/   r3   �	DoNothing�   s    ri   c             C   s   dS )NrG   r/   )r>   r?   r/   r/   r3   �ContinueEvent�   s    rj   N)rD   rF   rH   rE   rg   rh   ri   rj   r/   r/   r/   r3   �<module>�   s   0