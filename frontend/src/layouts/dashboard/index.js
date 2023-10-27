import { useEffect, useState, useContext } from 'react'
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";
import api from '../../api'
// Argon Dashboard 2 MUI components
import ArgonBox from "components/ArgonBox";
import ArgonTypography from "components/ArgonTypography";
import Card from "@mui/material/Card";

// Argon Dashboard 2 MUI example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import DetailedStatisticsCard from "examples/Cards/StatisticsCards/DetailedStatisticsCard";
import SalesTable from "examples/Tables/SalesTable";
import CategoriesList from "examples/Lists/CategoriesList";
import GradientLineChart from "examples/Charts/LineCharts/GradientLineChart";
import Table from "examples/Tables/Table";

// Argon Dashboard 2 MUI base styles
import typography from "assets/theme/base/typography";

// Dashboard layout components
import Slider from "layouts/dashboard/components/Slider";

// Data
import gradientLineChartData from "layouts/dashboard/data/gradientLineChartData";
import salesTableData from "layouts/dashboard/data/salesTableData";
import categoriesListData from "layouts/dashboard/data/categoriesListData";
import authorsTableData from "layouts/tables/data/authorsTableData";
import AuthContext from "context/AuthContext";

function Default() {
  const { columns, rows } = authorsTableData;
  const { user } = useContext(AuthContext)
  const [daysOff, setDaysOff] = useState([])
  const { size } = typography;

  useEffect(() => {
    getDaysOff();
    // deleteDayOff();
    // createDayoff();
    updateDayoff();
  }, [])

  // GET days off
  const getDaysOff = async () => {
    try {
      const response = await api.get('days-off/')
      setDaysOff(response.data)
    } catch (e) {
      console.error(e)
    }
  }

  // DELETE days off
  const deleteDayOff = async () => {
    try {
      const response = await api.delete('delete-day-off/30')

    } catch (e) {
      console.error(e)
    }
  }

  const createDayoff = async () => {
    try {
      const response = await api.post('days-off/',{
        user: user.user_id,
        start_date: "2023-10-11T06:53:52Z",
        end_date: "2023-10-11T06:53:52Z",
        off_type: "annual",
        dayoff_reason: "test reasone",
        status: "in_review",
      })
    } catch (e) {
      console.error(e)
    }
  } 

  const updateDayoff = async () => {
    try {
      const response = await api.put('update-day-off/5',{
        user: user.user_id,
        start_date: "2023-10-11T06:53:52Z",
        end_date: "2023-10-11T06:53:52Z",
        off_type: "annual",
        dayoff_reason: "EDITED",
        status: "in_review",
      })
    } catch (e) {
      console.error(e)
    }
  } 
  return (
    <DashboardLayout>
      <DashboardNavbar />
      <ArgonBox py={3}>
        <Grid container spacing={3} mb={3}>
          <Grid item xs={12} md={6} lg={3}>
            <DetailedStatisticsCard
              title="Kullanılan İzinler"
              count={daysOff.filter(item => item.off_type === "annual").length}
              icon={{ color: "info", component: <i className="ni ni-money-coins" /> }}
              percentage={{ color: "success", count: 14 - daysOff.filter(item => item.off_type === "annual").length, text: "Kalan" }}
            />

          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <DetailedStatisticsCard
              title="Bounce İzinleri"
              count={daysOff.filter(item => item.off_type === "bounce").length}
              icon={{ color: "error", component: <i className="ni ni-world" /> }}
              percentage={{ color: "success", count: 6 - daysOff.filter(item => item.off_type === "bounce").length, text: "Kalan" }}
            />
          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <DetailedStatisticsCard
              title="new clients"
              count="+3,462"
              icon={{ color: "success", component: <i className="ni ni-paper-diploma" /> }}
              percentage={{ color: "error", count: "-2%", text: "since last quarter" }}
            />
          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <DetailedStatisticsCard
              title="sales"
              count="$103,430"
              icon={{ color: "warning", component: <i className="ni ni-cart" /> }}
              percentage={{ color: "success", count: "+5%", text: "than last month" }}
            />
          </Grid>
        </Grid>
        <Grid container spacing={3} mb={3}>
          <Grid item xs={12} md={12}>
            <ArgonBox>
              <Card>
                <ArgonBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
                  <ArgonTypography variant="h6">İzinde Olan Personeller</ArgonTypography>
                </ArgonBox>
                <ArgonBox
                  sx={{
                    "& .MuiTableRow-root:not(:last-child)": {
                      "& td": {
                        borderBottom: ({ borders: { borderWidth, borderColor } }) =>
                          `${borderWidth[1]} solid ${borderColor}`,
                      },
                    },
                  }}
                >
                  <Table columns={columns} rows={rows} />
                </ArgonBox>
              </Card>
            </ArgonBox>
          </Grid>
        </Grid>
        <Grid container spacing={3}>
          <Grid item xs={12} md={8}>
            <SalesTable title="Sales by Country" rows={salesTableData} />
          </Grid>
          <Grid item xs={12} md={4}>
            <CategoriesList title="categories" categories={categoriesListData} />
          </Grid>
        </Grid>
      </ArgonBox>
      <div>
        {daysOff.map((item, index)=>(
          <p key={index}>{item.dayoff_reason}</p>
        ))}
      </div>
      <Footer />
    </DashboardLayout>
  );
}

export default Default;
