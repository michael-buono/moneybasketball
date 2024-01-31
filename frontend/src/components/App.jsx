import { useState } from 'react';

import {
  AppShell,
  Navbar,
  Header,
  Footer,
  Text,
  MediaQuery,
  Burger,
  Button,
  useMantineTheme,
  Paper
} from '@mantine/core';
import { Route, Routes, Link, useLocation } from 'react-router-dom';
import ApiTest from './ApiTest.jsx';

export default function App() {
  const location = useLocation();
  const theme = useMantineTheme();
  const [opened, setOpened] = useState(false);
  const navLinks = [
    { label: 'Home', path: '/' },
    { label: 'API Test', path: '/api-test' },
  ];
  const initialActiveLink = navLinks.find((link) => link.path === location.pathname)?.label || 'Home';
  const [activeLink, setActiveLink] = useState(initialActiveLink); // Default active link

  const links = navLinks.map((link) => (
    <Paper key={link.label} padding="xs" style={{ marginBottom: '8px', cursor: 'pointer' }}>
      <Button key={link.label} href="#" data-active={activeLink === link.label || undefined}  component={Link} to={link.path} variant={activeLink === link.label ? 'filled' : 'link'} onClick={() => setActiveLink(link.label)}>
        {link.label}
      </Button>
      </Paper>
  ));
  return (
      <AppShell
        styles={{
          main: {
            background: theme.colorScheme === 'dark' ? theme.colors.dark[8] : theme.colors.gray[0],
          },
        }}
        navbarOffsetBreakpoint="sm"
        navbar={
          <Navbar p="md" hiddenBreakpoint="sm" hidden={!opened} width={{ sm: 200, lg: 300 }}>
            {links}
          </Navbar>
        }
        footer={
          <Footer height={60} p="md">
            Application footer
          </Footer>
        }
        header={
          <Header height={{ base: 50, md: 70 }} p="md">
            <div style={{ display: 'flex', alignItems: 'center', height: '100%' }}>
              <MediaQuery largerThan="sm" styles={{ display: 'none' }}>
                <Burger
                  opened={opened}
                  onClick={() => setOpened((o) => !o)}
                  size="sm"
                  color={theme.colors.gray[6]}
                  mr="xl"
                />
              </MediaQuery>

              <Text>NBA Shot Diet</Text>
            </div>
          </Header>
        }
      >
        <Routes>
          <Route path="/api-test" element={<ApiTest />} />
          <Route path="/" element={<Text>NBA Shot Diet</Text>} />
        </Routes>
      </AppShell>
  );
};
