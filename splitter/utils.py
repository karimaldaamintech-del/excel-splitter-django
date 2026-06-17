import io
import zipfile
import pandas as pd

def split_excel_to_zip(file_content, rows_per_file=9998):
    xl = pd.ExcelFile(io.BytesIO(file_content))
    sheet_name = xl.sheet_names[0]
    df = pd.read_excel(xl, sheet_name=sheet_name, dtype=str)
    
    total_rows = len(df)
    if total_rows == 0:
        return None

    parts = (total_rows // rows_per_file) + (1 if total_rows % rows_per_file else 0)
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i in range(parts):
            start = i * rows_per_file
            end = start + rows_per_file
            chunk = df.iloc[start:end]
            
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                chunk.to_excel(writer, index=False)
            
            file_name = f"split_part_{i+1}.xlsx"
            zip_file.writestr(file_name, output.getvalue())
            
    zip_buffer.seek(0)
    return zip_buffer.getvalue()