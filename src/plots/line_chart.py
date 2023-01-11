import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo


class ScatterChartTrace:

    def __init__(self,
                 mode="lines+markers",  # either of 'lines+markers', 'markers', 'lines'
                 xaxis_data=np.linspace(1, 10, 10),
                 yaxis_data=np.linspace(1, 10, 10),
                 linecolour="red",
                 linewidth=2,
                 linestyle="solid",  # either of ‘solid’, ‘dot’, ‘dash’, ‘longdash’, ‘dashdot’, ‘longdashdot’
                 showlegend=True,
                 text_position="outside",
                 additional_text="mia xara",
                 text_colour="#000000",
                 textfont_family="Arial Black"):

        self.trace = self.__make_trace(
            mode=mode,
            xaxis_data=xaxis_data,
            yaxis_data=yaxis_data,
            linecolour=linecolour,
            linewidth=linewidth,
            linestyle=linestyle,
            showlegend=showlegend,
            text_position=text_position,
            additional_text=additional_text,
            text_colour=text_colour,
            textfont_family=textfont_family
        )

    @staticmethod
    def __make_trace(
            mode,
            xaxis_data,
            yaxis_data,
            linecolour,
            linewidth,
            linestyle,
            showlegend,
            text_position,
            additional_text,
            text_colour,
            textfont_family
    ):
        trace = go.Scatter(
            mode=mode,
            x=xaxis_data,
            y=yaxis_data,
            line=dict(
                color=linecolour,
                width=linewidth,
                dash=linestyle
            ),
            showlegend=showlegend,
            hoveron="points",
            hovertext="mia xara",
            # text=yaxis_data
        )
        return trace


class ScatterChartLayout:

    def __init__(self,
                 title_color="green",
                 title_font="Arial",
                 title_font_size=20,
                 title_text="My plot",
                 title_position=0.5,
                 xaxis_title="xaxis title",
                 yaxis_title="yaxis title",
                 bargap=0.2,
                 bargroupgap=0.1,
                 xaxis_tickmode="array",
                 xaxis_tickvals=np.linspace(1, 10, 10),
                 xaxis_ticktext=np.array(["5min", "10min", "15min", "20min"]),
                 paper_bgcolor="#ffffff",
                 plot_bgcolor="#ffffff"):

        self.layout = self.__make_layout(
            title_color=title_color,
            title_font=title_font,
            title_font_size=title_font_size,
            title_text=title_text,
            title_position=title_position,
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
            bargap=bargap,
            bargroupgap=bargroupgap,
            xaxis_tickmode=xaxis_tickmode,
            xaxis_tickvals=xaxis_tickvals,
            xaxis_ticktext=xaxis_ticktext,
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor
        )

    @staticmethod
    def __make_layout(
            title_color,
            title_font,
            title_font_size,
            title_text,
            title_position,
            xaxis_title,
            yaxis_title,
            bargap,
            bargroupgap,
            xaxis_tickmode,
            xaxis_tickvals,
            xaxis_ticktext,
            paper_bgcolor,
            plot_bgcolor
    ):
        layout = go.Layout(
            title=dict(
                font=dict(
                    color=title_color,
                    family=title_font,
                    size=title_font_size
                ),
                text=title_text,
                x=title_position
            ),
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
            bargap=bargap,
            bargroupgap=bargroupgap,
            xaxis=dict(
                tickmode=xaxis_tickmode,
                tickvals=xaxis_tickvals,
                ticktext=xaxis_ticktext
            ),
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor,
            hovermode="x unified"
        )
        return layout


class CreateFigure:

    def __init__(self,
                 traces,
                 layout,
                 show_fig=True,
                 yaxis_visible=True,
                 xaxis_visible=True):

        self.figure = self.__create_figure(
            traces=traces,
            layout=layout,
            yaxis_visible=yaxis_visible,
            xaxis_visible=xaxis_visible
        )

        if show_fig:
            pyo.plot(self.figure)

    @staticmethod
    def __create_figure(
            traces,
            layout,
            yaxis_visible,
            xaxis_visible
    ):
        figure = go.Figure(data=traces, layout=layout)

        figure.update_xaxes(
            showline=True,
            linewidth=2,
            linecolor="#000000"
        )

        figure.update_yaxes(
            showline=True,
            linewidth=2,
            linecolor="#000000"
        )

        if not yaxis_visible:
            figure.update_yaxes(visible=False)

        if not xaxis_visible:
            figure.update_xaxes(visible=False)

        return figure


if __name__ == "__main__":
    data_path = "C:\\Users\\Anast\\pythonProject\\Sales_Visual_Analytics\\data\\Sales.xls"
    df = pd.read_excel(data_path)
    test_df = df.loc[:20]
    test_df["extra"] = test_df["Sales"]*0.8

    trace1 = ScatterChartTrace(
        xaxis_data=test_df.index,
        yaxis_data=test_df["Sales"],
        linestyle="solid",
        linecolour="black",
        linewidth=3
    ).trace

    trace2 = ScatterChartTrace(
        xaxis_data=test_df.index,
        yaxis_data=test_df["extra"],
        linestyle="dot"
    ).trace

    fig = CreateFigure(
        traces=[trace1, trace2],
        layout=ScatterChartLayout().layout
    )
