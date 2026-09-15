Name:           postman
Version:        12.28.1
Release:        %autorelease
Summary:        Postman API Platform

License:        Proprietary
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

%description
Build, test, and document your APIs faster.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/postman
cp -a * %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -sr %{buildroot}/opt/postman/Postman %{buildroot}%{_bindir}/postman
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/pixmaps
ln -sr %{buildroot}/opt/postman/app/resources/app/assets/icon.png %{buildroot}%{_datadir}/pixmaps/postman.png

%check

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/pixmaps/postman.png

%changelog
%autochangelog
