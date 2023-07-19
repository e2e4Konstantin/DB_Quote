from data_tools import SourceData
from db_tools import dbControl

paths = {
    "home": r"F:\Kazak\Google Диск\1_KK\Job_CNAC\Python_projects\DB_Quote\src_data",
    "office": r" ",
}
source_files = {
    3: (r"template_3_68_output.xlsx", "Quote"),
    4: (r"template_4_68_output.xlsx", "Quote"),
    5: (r"template_5_67_output.xlsx", "Quote"),
}

fn = 3
pl = "home" # "office"
dset = (source_files[fn][0], paths[pl], source_files[fn][1])

if __name__ == "__main__":

    data = SourceData(*dset)
    print(data, "\n")
    print(data.df.info(verbose=True))
    print(f"непустых значений в столбце 'A': {data.df[data.df.columns[0]].count()}", "\n")

    x = dbControl("quote.sqlite")
    with x as db:
        x.inform_db()
