Summary:        Manage your sim card contacts with pcsc reader
Name:           monosim
Version:        1.3.0.1
Release:        %mkrel 2
License:        GPLv2
Group:          Office
Source:         http://www.integrazioneweb.com/monosim/packages/monosim-1.3.0.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
URL:            http://www.integrazioneweb.com/monosim

BuildArch:      noarch

BuildRequires:  gtk-sharp2-devel >= 2.8.3
BuildRequires:  glib-sharp2 >= 2.8.3
BuildRequires:  glade-sharp2 >= 2.8.3
BuildRequires:  mono-web >= 1.2.3
BuildRequires:  mono >= 1.2.3
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig

Requires:       gtk-sharp2 >= 2.8.3
Requires:       glib-sharp2 >= 2.8.3
Requires:       mono >= 1.2.3
Requires:       mono-web >= 1.2.3
Requires:       pcsc-lite
Requires:       libpcsclite1
Requires:       libpcsclite-devel

%define debug_package %{nil}

%description
is a simple application that can be used to read, write, update, delete and 
backup your sim card contacts. It open and save also some format files to 
manage your contacts also in a text files. To connect monosim to your 
smartcard you need use a standard PCSC smartcard reader as towitoko, acs,
athena, blutronics, etc.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} install
desktop-file-install --vendor="mandriva"               \
  --dir=%{buildroot}%{_datadir}/applications    \
  monoSIM/images/%{name}.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc readme
%doc copying.gpl
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mandriva-monosim.desktop


